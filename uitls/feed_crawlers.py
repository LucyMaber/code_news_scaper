from asyncio.tasks import ALL_COMPLETED, FIRST_COMPLETED
from re import T
import json
from bs4.builder import TreeBuilder
import requests
from urllib.parse import urlparse, urljoin
import asyncio
from bs4 import BeautifulSoup
import rdflib
import validators
import urllib.robotparser
import time
import enlighten
from uitls.enlightenPlus.cache import Cache
import tldextract
from uitls.reqest_man import is_crawl_delay, reqest_saferobot, setup_robot


FeedRdfTypes = [
    'application/rdf+xml',
    'text/rdf+xml',
    'text/rdf',
    'application/rdf',
    "application/ld+json",
    "application/trig",
    "text/n3",
    "application/n-triples",
]
FeedAtomTypes = [
    'application/atom+xml',
    'application/atom',
    'text/atom+xml',
    'text/atom',
]
FeedRssTypes = [
    'application/rss+xml',
    'application/rss',
    'text/rss+xml',
    'text/rss',
]
feedJsonTypes = [
    'application/feed+json',
    'text/feed+json',
]
HTMLTypes = [
    "application/x-hatom",
    "application/xhtml+xml",
    "application/html",
    "text/html",
    "html",
    "text/html; charset=utf-8",
    "text/html;charset=UTF-8"
]
FeedTypes = FeedRdfTypes+FeedAtomTypes+FeedRssTypes+feedJsonTypes+HTMLTypes
knownFeedEndpoints = [
    # '/ror.xml',
    "/",
    '/?feed=rss',
    '/?feed=rss2',
    '/?feed=rdf',
    '/?feed=atom',
    '/feed/',
    '/feed/rss/',
    '/feed/rss2/',
    '/feed/rdf/',
    '/feed/atom/',
    '/services/rss/',
    "/rss.xml",
    "/feed.xml",
    "/rss",
    "/atom",
    "/feed",
    "?alt=rss",
    "?service=rss",
    "?service=atom",
    "/newsfeed",
    "/rss-feed",
    "/rss.jsp",
    "/index.xml",
    'news/?feed=rss',
    'news/?feed=rss2',
    'news/?feed=rdf',
    'news/?feed=atom',
    'news/feed/',
    'news/feed/rss/',
    'news/feed/rss2/',
    'news/feed/rdf/',
    'news/feed/atom/',
    'news/services/rss/',
    "news/rss.xml",
    "news/feed.xml",
    "news/rss.php",
    "news/feed.php",
    "news/rss",
    "news/fv",
    "news/atom",
    "news/index.xml",
    "news/newsfeed",
    "news/rss-feed",
    # "text/x-opml"
]
coros = []


class WebStiteScrapeFeed:
    def __init__(self, sprql, count, feedspot) -> None:
        self.feedspot = feedspot
        self.sprql = sprql
        self.url = sprql["official_website"]
        self.places = []
        self.feed = []
        self.subhub = []
        self.seen = set()
        self.seenfeeds = set()
        self.x = {}
        self.count = count
        for Eurl in sprql["official_website"]:
            if "web.archive.org/" in Eurl:
                continue
            setup_robot(Eurl)
            self.places.append({"count": count, "where": Eurl, "href": Eurl})
        # for Eurl in sprql["web_feed_URL"]:
        #     self.places.append({"count": count, "where": Eurl, "href": Eurl})
        try:
            for Eurl in sprql["page_url"]:
                if "web.archive.org/" in Eurl:
                    continue
                self.places.append(
                    {"count": count, "where": Eurl, "href": Eurl})
        except:
            pass
        for knownFeedEndpoint in knownFeedEndpoints:
            for url in self.url:
                if "web.archive.org/" in url:
                    continue
                url = urllib.parse.urljoin(url, knownFeedEndpoint)
                self.places.append({"count": count, "where": url, "href": url})

    def robot_mtime(self):
        try:
            return self.rp.mtime()
        except:
            return None

    def robot_modified(self):
        try:
            return self.rp.modified()
        except:
            return None

    def robot_crawl_delay(self):
        try:
            return self.rp.crawl_delay()
        except:
            return 0

    def robot_request_rate(self):
        try:
            return self.rp.crawl_delay()
        except:
            return 0

    def robot_can_fetch(self, url):
        try:
            return self.rp.can_fetch("*", url)
        except:
            return None

    def robot_site_maps(self):
        try:
            return self.rp.site_maps()
        except:
            return None

    async def crawler_scan(self, place, r):
        r = await r
        if r is None:
            return
        try:
            if r is None:
                return
            # if r.status in [404, 401, 451, 410, 408, 510, 508, 501, 511]:
            #     return
            if "Content-type" in r.headers:
                mime = r.headers['Content-type']
            elif "type" in place.key():
                mime = place["type"]
            else:
                mime = ""
            for i in FeedAtomTypes:
                if i in mime:
                    try:
                        if self.scanAtom(r.contents(), place):
                            print("found= ", "FeedAtom")
                            return
                    except:
                        pass
            for i in FeedAtomTypes:
                if i in mime:
                    try:
                        if await self.scanRSS(r.contents(), place):
                            print("found= ", "rss")
                            return
                    except:
                        pass
            for i in FeedAtomTypes:
                if i in mime:
                    try:
                        if await self.scanJSONFeed(r.contents(), place):
                            print("found= ", "json")
                            return
                    except:
                        pass
            for i in HTMLTypes:
                if i in mime:
                    try:
                        if await self.scanHTML(r.contents(), place):
                            print("found= ", "html")
                            return
                    except:
                        pass
            # elif mime in HTMLTypes:
            #     try:
            #         if await asyncio.wait_for(self.scanSitemap(r.content, place), timeout=10):
            #             print("found= ","sitemap")
            #             return
            #     except:
            #         pass
            # elif mime in HTMLTypes:
            #     try:
            #         if await asyncio.wait_for(self.scanJSONFeed(r.content, place), timeout=10):
            #             print("found= ","JSONFeed")
            #             return
            #     except:
            #         pass
            else:
                if await asyncio.wait_for(self.scanHTML(r.contents(), place), timeout=10):
                    return
            if await asyncio.wait_for(self.scanHTML(r.contents(), place), timeout=10):
                return
            if await asyncio.wait_for(self.scanAtom(r.contents(), place), timeout=10):
                return
            if await asyncio.wait_for(self.scanRSS(r.contents(), place), timeout=10):
                return
            if await asyncio.wait_for(self.scanJSONFeed(r.contents(), place), timeout=10):
                return
            if await asyncio.wait_for(self.scanSitemap(r.contents(), place), timeout=10):
                return
            if await self.scanJSONFeed(r.contents(), place):
                return
        except Exception as e:
            print(e)

    async def crawler_fast_fach_scan(self, place):
        if place['href'].lower() in self.seen:
            return
        try:
            r = await reqest_saferobot(place["href"], retry_on_code=[403])
            self.crawler_scan(place, r)
        except:
            return

    async def crawler(self):
        feed = True
        has_done_common_crawl_index = True
        # crawlerSoite = Spinner('crawler spiner ')
        reqest_list = []
        while True:
            while len(self.places) != 0:
                # crawlerSoite.update()
                Fail = False
                place = self.places.pop()
                place_keys = place.keys()
                if place["href"] in self.x and len(self.places) != 0:
                    continue
                if place["href"].lower() in self.seen and len(self.places) != 0:
                    continue
                self.seen.add(place["href"].lower())
                self.x[place["href"]] = 1
                if "where" in place_keys and not validators.domain(place['href']):
                    place['href'] = urllib.parse.urljoin(
                        place['where'], place['href'])
                place['href'] = urllib.parse.urldefrag(place['href']).url
                if place["count"] == 0 and len(self.places) != 0:
                    continue
                elif len(self.places) != 0:
                    pass
                else:
                    print("count of places:", len(self.places))
                    print("count of :", len(self.feed))
                    print("count of seen:", len(self.seen))
                    print("count of feed:", len(self.feed))
                    print("count of subhub:", len(self.subhub))
                    print("count:", place["count"])
                    place["count"] = place["count"] - 1
                isDomainOrSub = False
                for url in self.url:
                    urlT1 = tldextract.extract(url)
                    urlT2 = tldextract.extract(place['href'])
                    if urlT2.domain == urlT1.domain:
                        isDomainOrSub = True
                    # the wayback Machine
                if not isDomainOrSub and len(self.places) != 0:
                    continue
                r = reqest_saferobot(place["href"], retry_on_code=[403])
                reqest_list.append(self.crawler_scan(place, r))

            if len(reqest_list) != 0:
                await asyncio.gather(*reqest_list)
                reqest_list = []
                continue
            if has_done_common_crawl_index:
                if len(self.sprql["common_crawl"]) == 0:
                    for code in asyncio.gather(self.sprql["common_crawl"]):
                        for i in code:
                            print(i)
                has_done_common_crawl_index = False
            else:
                break

    def scanSitemap(self, content, place):
        isGood = False
        try:
            soup = BeautifulSoup(content, 'xml')
            for sitemap in soup.select('sitemap'):
                isGood = True
                for loc in sitemap.select('loc'):
                    if loc.text not in self.seen:
                        self.places.append(
                            {"where":  loc.text, "count": place["count"]+1, "href": loc.text})
            for url in soup.select('url'):
                for loc in url.select('loc'):
                    isGood = True
                    if loc.text not in self.seen:
                        self.places.append(
                            {"where":  loc.text, "count": place["count"]+1, "href": loc.text})
        except:
            return False
        return isGood

    def scanHTML(self, content, place):
        isGood = False
        isFeed = False
        soup = BeautifulSoup(content, 'html.parser')
        # hAtom
        try:
            for hfeed in (soup.select('[rel="hfeed"],.hfeed')):
                for hentry in hfeed.select('[rel="hentry"],.hentry'):
                    for bookmark in hentry.select('[rel="bookmark"], .bookmark'):
                        if bookmark.has_attr("href") and validators.url(bookmark['href']):
                            url = urljoin(place["href"], bookmark["href"])
                            link = {"count": place["count"],
                                    "where": bookmark["href"],
                                    "href": url}
                            if link["href"] not in self.seen:
                                self.places.append(link)
                            isFeed = True
        except:
            pass
        # hslice
        try:
            for hslice in (soup.select('[rel="hslice"],.hslice')):
                for bookmark in hslice.select('[rel="bookmark"], .bookmark'):
                    if bookmark.has_attr("href"):
                        url = urljoin(place["href"], bookmark["href"])
                        link = {
                            "count": place["count"], "where": bookmark["href"], "href": url}
                        self.feed.append(link)
                        isFeed = True
        except:
            pass
        # Scan for LINKS
        for i in (soup.select('area ,link ,a')):
            isGood = True
            url = urljoin(place["href"], i["href"])
            link = {"count": place["count"],
                    "where": url, "href": url}
            if i.has_attr('type'):
                pass
            if i.has_attr('rel'):
                if "stylesheet" in i["rel"]:
                    continue
                if "modulepreload" in i["rel"]:
                    continue
                if "manifest" in i["rel"]:
                    continue
                if "hub" in i["rel"]:
                    for x in (soup.select('area ,link ,a')):
                        if "self" in x["hub"]:
                            self.subhub.append(
                                {"hub": i["href"], "self": x["href"]})
                    continue
                if "license" in i["rel"]:
                    continue
                if "noreferrer" in i["rel"]:
                    continue
                if "help" in i["rel"]:
                    continue
                if "icon" in i["rel"]:
                    continue
                if "canonical" in i["rel"]:
                    continue
                if "author" in i["rel"]:
                    continue
                if "dns-prefetch" in i["rel"]:
                    continue
                link["rel"] = i["rel"]
            if i.has_attr('type'):
                if i["type"] in FeedTypes:
                    self.feed.append(link)
                else:
                    continue
            if link["href"] not in self.seen:
                self.places.append(link)
        if isFeed:
            place["type"] = "HTML_Feed"
            if place["href"] not in self.seenfeeds:
                self.seenfeeds.add(place["href"])
                self.feed.append(place)
            isGood = True
        return isGood

    async def scanRSS(self, content, place):
        isGood = False
        soup = BeautifulSoup(content, features='xml')
        articles = soup.findAll('item')
        for a in articles:
            url = urljoin(place["href"], place["href"])
            link = {"count": place["count"], "href": url, "where": url}
            if link["href"] not in self.seen:
                self.places.append(link)
        if isGood:
            place["type"] = "RSS"
            if place["href"] not in self.seenfeeds:
                self.seenfeeds.add(place["href"])
                self.feed.append(place)
        return isGood

    async def scanAtom(self, content, place):
        isGood = False
        soup = BeautifulSoup(content, 'xml')
        for feed in soup.select('feed'):
            for i in feed.select('link'):
                isGood = True
                try:
                    url = urljoin(place["href"], place["href"])
                    link = {"count": place["count"],
                            "where": i["href"], "href": url}
                    if place["href"] not in self.seen:
                        self.places.append(link)
                except:
                    pass
        if isGood:
            place["type"] = "Atom"
            if place["href"] not in self.seenfeeds:
                self.seenfeeds.add(place["href"])
                self.feed.append(place)
        return isGood

    def scanJSONFeed(self, content, place):
        isGood = False
        try:
            content = json.loads(content)
            for item in content["items"]:
                url = urljoin(item["url"], place["href"])
                link = {"count": place["count"],
                        "where": item["url"], "href": url}

            if place["href"] not in self.seenfeeds:
                self.seenfeeds.add(place["href"])
            if place["href"] not in self.seen:
                self.places.append(link)
                isGood = True
        except:
            pass
        if isGood:
            place["type"] = "JSONFeed"
            if place["href"] not in self.seenfeeds:
                self.seenfeeds.add(place["href"])
                self.feed.append(place)
        return isGood

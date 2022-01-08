from asyncio.tasks import ALL_COMPLETED, FIRST_COMPLETED
from re import T
import json
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
from uitls.reqest_man import is_crawl_delay, reqest_saferobot


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
    "text/html; charset=utf-8"
]
FeedTypes = FeedRdfTypes+FeedAtomTypes+FeedRssTypes+feedJsonTypes+HTMLTypes
knownFeedEndpoints = [
    '/ror.xml',
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
    "news/feed",
    "news/atom",
    "news/index.xml",
    "news/newsfeed",
    "news/rss-feed",
    "text/x-opml"
]
coros = []


class WebStiteScrapeFeed:
    def __init__(self, sprql, count,) -> None:
        self.url = sprql["official_website"]
        self.places = []
        self.feed = []
        self.seen = []
        self.x = {}
        self.count = count
        for Eurl in sprql["web_feed_URL"]:
            self.places.append({"count": count, "where": Eurl, "href": Eurl})
        for Eurl in sprql["web_feed_URL"]:
            self.feed.append({"count": count, "where": Eurl, "href": Eurl})
        for Eurl in sprql["page_url"]:
            self.places.append({"count": count, "where": Eurl, "href": Eurl})
        for knownFeedEndpoint in knownFeedEndpoints:
            for url in self.url:
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
        try:
            if r is None:
                return
            if r.content is None:
                return
            if len(r.content) == 0:
                return
            if len(r.content) in [404, 401, 451, 410, 408, 510, 508, 501, 511]:
                return
            if "Content-type" in r.headers.keys():
                mime = r.headers['Content-type']
            else:
                mime = ""
            # if mime in FeedRdfTypes or "rdf" in place["type"]:  # scanJSONFeed
            #     pass
                # await asyncio.wait_for(self.scanRDF(r.content, place), timeout=60)
            if mime in FeedAtomTypes:
                if await asyncio.wait_for(self.scanAtom(r.content, place), timeout=10):
                    print("found= ","FeedAtom")
                    return
            elif mime in FeedRssTypes or "rss" in place["type"]:
                if await asyncio.wait_for(self.scanRSS(r.content, place), timeout=10):
                    print("found= ","rss")
                    return
            elif mime in feedJsonTypes or "json" in place["type"]:
                if await asyncio.wait_for(self.scanJSONFeed(r.content, place), timeout=10):
                    print("found= ","json")
                    return
            elif mime in HTMLTypes or "html" in place["type"]:
                if await asyncio.wait_for(self.scanHTML(r.content, place), timeout=10):
                    print("found= ","html")
                    return
            elif mime in HTMLTypes or "sitemap" in place["type"]:
                if await asyncio.wait_for(self.scanSitemap(r.content, place), timeout=10):
                    print("found= ","sitemap")
                    return
            elif mime in HTMLTypes or "JSONFeed" in place["type"]:
                if await asyncio.wait_for(self.scanJSONFeed(r.content, place), timeout=10):
                    print("found= ","JSONFeed")
                    return
            else:
                if await asyncio.wait_for(self.scanHTML(r.content, place), timeout=10):
                    return
            if await asyncio.wait_for(self.scanHTML(r.content, place), timeout=10):
                return
            if await asyncio.wait_for(self.scanAtom(r.content, place), timeout=10):
                return
            if await asyncio.wait_for(self.scanRSS(r.content, place), timeout=10):
                return
            if await asyncio.wait_for(self.scanJSONFeed(r.content, place), timeout=10):
                return
            if await asyncio.wait_for(self.scanSitemap(r.content, place), timeout=10):
                return
            if await asyncio.wait_for(self.scanJSONFeed(r.content, place), timeout=10):
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
        # crawlerSoite = Spinner('crawler spiner ')
        while len(self.places) != 0:
            # crawlerSoite.update()
            Fail = False
            place = self.places.pop()
            place_keys = place.keys()
            print(place_keys)
            if place["href"] in self.x:
                continue
            if place["href"].lower() in self.seen:
                continue
            self.seen.append(place["href"].lower())
            self.x[place["href"]] = 1
            if "where" in place_keys and not validators.domain(place['href']):
                place['href'] = urllib.parse.urljoin(
                    place['where'], place['href'])
            place['href'] = urllib.parse.urldefrag(place['href']).url
            if place["count"] == 0:
                continue
            else:
                print("count of places:", len(self.places))
                print("count of :", len(self.feed))
                print("count of seen:", len(self.seen))
                print("count of feed:", len(self.feed))
                print("count:", place["count"])
                place["count"] = place["count"] - 1
            isDomainOrSub = False
            for url in self.url:
                urlT1 = tldextract.extract(url)
                urlT2 = tldextract.extract(place['href'])
                if urlT2.domain == urlT1.domain:
                    isDomainOrSub =True
                #the wayback Machine 
            if not isDomainOrSub:
                continue
            r = await reqest_saferobot(place["href"], retry_on_code=[403])
            if r is not None:
                print(r)
                await self.crawler_scan(place, r)
                if len(self.places) == 0:
                    break

    def scanSitemap(self, content, place):
        isGood = False
        try:
            soup = BeautifulSoup(content, 'xml')
            for sitemap in soup.select('sitemap'):
                isGood = True
                for loc in sitemap.select('loc'):
                    self.places.append(
                        {"where":  loc.text, "count": place["count"]+1})
            for url in soup.select('url'):
                for loc in url.select('loc'):
                    isGood = True
                    self.places.append(
                        {"where":  loc.text, "count": place["count"]+1})
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
                            url =urljoin(place["href"],bookmark["href"])
                            link = {"count": place["count"],
                                    "where": bookmark["href"],
                                    "href":url}
                            self.places.append(link)
                            isFeed = True
        except:
            pass
        # hslice
        try:
            for hslice in (soup.select('[rel="hslice"],.hslice')):
                for bookmark in hslice.select('[rel="bookmark"], .bookmark'):
                    if bookmark.has_attr("href"):
                        url =urljoin(place["href"],bookmark["href"])
                        link = {
                            "count": place["count"], "where": bookmark["href"], "href": url}
                        self.feed.append(link)
                        isFeed = True
        except:
            pass
        # Scan for LINKS
        for i in (soup.select('area ,link ,a')):
            print(i)
            isGood = True
            url =urljoin(place["href"],bookmark["href"])
            link = {"count": place["count"],
                    "where":url, "href": url}
            if i.has_attr('type'):
                pass
            if i.has_attr('rel'):
                if "stylesheet" in i["rel"]:
                    continue
                if "modulepreload" in i["rel"]:
                    continue
                if "manifest" in i["rel"]:
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
            self.places.append(link)
        if isFeed:
            place["type"] = "HTML_Feed"
            self.feed.append(place)
            isGood = True
        return isGood

    async def scanRSS(self, content, place):
        isGood = False
        soup = BeautifulSoup(content, features='xml')
        articles = soup.findAll('item')
        for a in articles:
            url =urljoin(place["href"],place["href"])
            link = {"count": place["count"], "href": url, "where":url}
            self.places.append(link)
        if isGood:
            place["type"] = "Atom"
            self.feed.append(place)
        return isGood

    async def scanAtom(self, content, place):
        isGood = False
        soup = BeautifulSoup(content, 'xml')
        for feed in soup.select('feed'):
            for i in feed.select('link'):
                isGood = True
                try:
                    print(i)
                    url =urljoin(place["href"],place["href"])
                    link = {"count": place["count"],
                            "where": i["href"], "href":url}
                    self.places.append(link)
                except:
                    pass
        if isGood:
            place["type"] = "Atom"
            self.feed.append(place)
        return isGood

    async def scanJSONFeed(self, content, place):
        isGood = False
        try:
            content = json.loads(content)
            for item in content["items"]:
                url =urljoin( item["url"],place["href"])
                link = {"count": place["count"],
                        "where": item["url"], "href": url}
                self.places.append(link)
                isGood = True
        except:
            pass
        if isGood:
            place["type"] = "JSONFeed"
            self.feed.append(place)
        return isGood

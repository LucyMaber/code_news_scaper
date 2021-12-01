from re import T
import requests
from urllib.parse import urlparse, urljoin
import asyncio
from bs4 import BeautifulSoup
import rdflib
import validators
import urllib.robotparser
import time


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
    def __init__(self, url, count, Eurls = []) -> None:
        self.url = url
        self.places = []
        self.feed = []
        self.seen = []
        self.count = count
        self.places.append({"href": url, "count": count})
        for Eurl in Eurls:
            self.places.append( {"count": count, "where": Eurl, "href": Eurl})
        for knownFeedEndpoint in knownFeedEndpoints:
            aurl = urllib.parse.urljoin(url, knownFeedEndpoint)
            self.places.append(
                {"count": count, "where": aurl, "href": aurl, "type": "sitemap"})
        try:
            self.rp = urllib.robotparser.RobotFileParser()
            self.rp.set_url(url+"/robots.txt")
            self.rp.read()
            for url_sitemap in self.robot_site_maps():
                self.places.append(
                    {"count": count, "where": url_sitemap, "href": url_sitemap, "type": "sitemap"})
            self.robot = True
        except:
            self.robot = False

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
        mime = r.headers['Content-type']
        place['type'] = mime
        if mime in FeedRdfTypes or "rdf" in place["type"]:
            await asyncio.wait_for(self.scanRDF(r.content, place), timeout=60)
        elif mime in FeedAtomTypes:
            await asyncio.wait_for(self.scanAtom(r.content, place), timeout=60)
        elif mime in FeedRssTypes or "rss" in place["type"]:
            await asyncio.wait_for(self.scanRSS(r.content, place), timeout=60)
        elif mime in feedJsonTypes or "json" in place["type"]:
            await asyncio.wait_for(self.scanJSONFeed(r.content, place), timeout=60)
        elif mime in HTMLTypes or "html" in place["type"]:
            await asyncio.wait_for(self.scanHTML(r.content, place), timeout=60)
        else:
            pass

    async def crawler_fast_fach_scan(self, place):
        if place['href'] in self.seen:
            return
        else:
            self.seen.append(place['href'])
        try:
            r = requests.get(place["href"],timeout=(3.05, 27))
            self.crawler_scan(place, r)
        except:
            return

    async def crawler(self):
        crawler_list = []
        while len(self.places) != 0 or len(crawler_list) != 0:
            print(len(self.places))
            Fail = False
            place = self.places.pop()
            place_keys = place.keys()
            if "where" in place_keys and not validators.domain(place['href']):
                place['href'] = urllib.parse.urljoin(
                    place['where'], place['href'])
            place['href'] = urllib.parse.urldefrag(place['href']).url
            if place["count"] >= 0:
                place["count"] = place["count"] - 1
            else:
                continue
            domain = urlparse(self.url).netloc
            href = urlparse(place['href']).netloc
            if not href in domain:
                continue

            if domain == href:
                has_robot_daly = self.robot
                if not self.robot_can_fetch(place['href']):
                    continue
                time.sleep(self.robot_crawl_delay())
            else:
                url_rbot = urllib.parse.urljoin(place['href'], "/robots.txt")
                try:
                    rp = urllib.robotparser.RobotFileParser()
                    rp.set_url(url_rbot)
                    rp.read()
                    rate = rp.request_rate("*")
                    if not rp.set_url(place['href']):
                        has_robot_daly = True
                        continue
                    if rate is not None:
                        time.sleep(rate)
                    else:
                        has_robot_daly = False
                except:
                    pass
            if has_robot_daly:
                try:
                    r = requests.get(place["href"], timeout=(5, 10))
                    crawler_list.append(asyncio.create_task(
                        self.crawler_scan(place, r)))
                except:
                    continue
            else:
                crawler_list.append(asyncio.create_task(
                    self.crawler_fast_fach_scan(place)))
            if len(self.places) == 0:
                done, pending = await asyncio.wait(crawler_list)
                crawler_list = []
                if len(crawler_list) != 0:
                    break

    def sitemap(self, content, place):
        try:
            soup = BeautifulSoup(content, 'lxml')
            for urlset in soup.select('sitemap , urlset'):
                for sitemap in urlset.select('sitemapindex'):
                    self.places.append(
                        {"where": place["href"], "href": sitemap.getText(), "type": "sitemap", "count": place["count"]})
                for url in urlset.select('url'):
                    self.places.append(
                        {"where": place["href"], "href": sitemap.getText(), "type": "sitemap", "count": place["count"]})
            return True
        except:
            return False

    def XBEL(self, content, url, count, place):
        try:
            soup = BeautifulSoup(content, 'lxml')
            for opml in soup.select('opml'):
                for body in opml.select('body'):
                    for outline in body.select('outline'):
                        if outline.has_attr('xmlUrl'):
                            self.places.append({outline["xmlUrl"]})
                        if outline.has_attr('htmlUrl'):
                            self.places.append({outline["htmlUrl"]})
                        if outline.has_attr('url'):
                            self.places.append({outline["url"]})
            return True
        except:
            return False

    async def scanHTML(self, content, place):
        isGood = False
        try:
            soup = BeautifulSoup(content, 'html.parser')
            hasContent = False
            # hAtom
            for hfeed in (soup.select('[rel="hfeed"],.hfeed')):
                for hentry in hfeed.select('[rel="hentry"],.hentry'):
                    for bookmark in hentry.select('[rel="bookmark"], .bookmark'):
                        hasContent = True
                        link = {"count": place["count"],
                                "where": place["href"]}
                        if bookmark.has_attr("href") and validators.url(bookmark['href']):
                            link["href"] = bookmark["href"]
                    for tag in hentry.select('[rel="tag"],.tag'):
                        hasContent = True
                        link = {"count": place["count"],
                                "where": place["href"]}
                        if tag.has_attr("href") and validators.url(tag['href']):
                            link["href"] = tag["href"]
            # hslice
            for hslice in (soup.select('[rel="hslice"],.hslice')):
                for bookmark in hslice.select('[rel="bookmark"], .bookmark'):
                    try:
                        if bookmark.has_attr("href") and validators.url(bookmark['href']):
                            link["href"] = bookmark["href"]
                    except:
                        pass
                for feedurl in hslice.select('[rel="feedurl"], .feedurl'):
                    try:
                        link = {"count": place["count"],
                                "where": place["href"]}
                        if feedurl.has_attr("href") and validators.url(feedurl['href']):
                            link["href"] = tag["href"]
                    except:
                        pass

            if hasContent and place["href"] not in self.seen:
                self.feed.append(
                    {"type": "hfeed", "url": place["href"], "count": place["count"]})
            # Scan for LINKS
            for i in (soup.select('area ,link ,a')):
                link = {"count": place["count"], "where": place["href"]}
                try:
                    link["href"] = i["href"]
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
                        link["type"] = i["type"]
                        if i["type"] in FeedTypes and place["href"] not in self.seen:
                            self.feed.append(link)
                            self.seen.append(link)
                        else:
                            continue
                    self.places.append(link)
                except:
                    pass
            return isGood
        except:
            return False

    async def scanRSS(self, content, place):
        isGood = False
        try:
            soup = BeautifulSoup(content, 'lxml')
            for rss in soup.select('rss'):
                for channel in rss.select('channel'):
                    for item in channel.select('item'):
                        for i in item.select('link'):
                            link = {"count": place["count"],
                                    "where": place["href"]}
                            try:
                                link["href"] = i.get_text()
                                self.places.append(link)
                            except:
                                pass
            if not place["href"] not in self.seen and isGood:
                self.feed.append(place)
                self.seen.append(place["href"])
            return isGood
        except:
            return False

    async def scanAtom(self, content, place):
        isGood = False
        try:
            soup = BeautifulSoup(content, 'lxml')
            for feed in soup.select('feed'):
                for entry in feed.select('entry'):
                    for i in feed.select('link'):
                        isGood = True
                        link = {"count": place["count"], "where": place["href"]}
                        try:
                            link["href"] = link["href"]
                            self.places.append(link)
                        except:
                            pass
            if not place["href"] not in self.seen and isGood:
                self.feed.append(place)
                self.seen.append(place["href"])
            return isGood
        except:
            return False

    async def scanRDF(self, content, place):
        isGood = False
        try:
            graph = rdflib.Graph()
            graph.parse(place["href"])
            for subj, pexternalDomain, obj in graph:
                if (validators.url(str(obj))):
                    link = {"count": place["count"], "where": place["href"]}
                    try:
                        isGood = True
                        link["href"] = obj
                        self.feed.append(link)
                    except:
                        pass
            place["type"].append("RDF")
            if not place["href"] not in self.seen and isGood:
                self.feed.append(place)
                self.seen.append(place["href"])
            return isGood
        except:
            return False

    async def scanJSONFeed(self, content, place):
        isGood = False
        try:
            content["version"]
            content["title"]
            for item in content["items"]:
                item["id"]
                if (validators.url(str(item["url"]))):
                    link = {"count": place["count"], "where": place["href"]}
                    isGood = True
                    try:
                        link["href"] = item["url"]
                        if not place["href"] not in self.seen:
                            self.places.append(link)
                    except:
                        pass
            place["type"].append("JSONFeed")
            if not place["href"] not in self.seen and isGood:
                self.feed.append(place)
                self.seen.append(place["href"])
            return isGood
        except:
            return False

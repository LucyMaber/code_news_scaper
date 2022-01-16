from asyncio.tasks import sleep
import asyncio
from re import T
from urllib.parse import urljoin, urlparse
import aiohttp
from aiohttp import ClientSession
import dns.asyncresolver
import json
from bs4 import BeautifulSoup
import urllib.robotparser
import time
import json
# from pymongo import MongoClient
# client = MongoClient(port=27017)
# db=client.web_scrape

sites = {}

URLLookups = {}
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) FeedScaner",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "TE": "trailers",
    "content-length": "0"
}


class FakeReqest:
    async def createCashes(self, text, status) -> None:
        self._text = text
        self._status = status

    async def create(self, response) -> None:
        self._text = await response.text()
        self._status = response.status
        self.headers = response.headers

    def json(self):
        return json.loads(self._text)

    def text(self):
        return self._text

    def contents(self):
        return self._text

    def status(self):
        return self._status


async def reqests_saferobots(urls, bot=True, rate=0, retry_on_code=[], caching_hard=False):
    for url in urls:
        print("looking at ", url)
        async with ClientSession() as client:
            ret = await CacheLoad(url)
            if ret is not None:
                print("found in cashe url:", url)
                return ret
            o = urlparse(url)
            if o.scheme == 'mailto':
                return None
            elif o.scheme == '':
                pass
            elif o.scheme == 'http':
                pass
            elif o.scheme == 'https':
                pass
            else:
                return None

            if True:
                try:

                    if not o.netloc in sites.keys():

                        result = await dns.asyncresolver.resolve(o.netloc)
                    else:
                        if not sites[o.netloc]["DNS"]:
                            return None
                except:
                    sites[o.netloc] = {}
                    sites[o.netloc]["DNS"] = False
                    return None
            await setup_robot(url)

            if sites[o.netloc]["robots"] is not None:
                sites[o.netloc]["robots"].can_fetch("*", url)

            if is_crawl_delay(url):
                timeout = sites[o.netloc]["robots"].crawl_delay("*")
                timeout = timeout + rate
            else:
                timeout = rate
            await sites[o.netloc]["Lock"].acquire()
            if timeout != 0:
                await rate_sleep(o, timeout)
            for i in range(10):
                if True:
                    try:
                        print("trying  url:", url, " Timeout:",
                              timeout, " count", i)
                        async with client.get(url) as response:
                            print("url:", url, " status:", response.status)
                            if response.status in [404, 401, 451, 410, 408, 510, 508, 501, 511]:
                                if sites[o.netloc]["Lock"].locked():
                                    sites[o.netloc]["Lock"].release()
                                co = FakeReqest()
                                await CacheStore(caching_hard, url, response)
                                await co.create(response)
                                sites[o.netloc]["timeout"] = time.time()
                                return co
                            elif response.status in retry_on_code or response.status in [500, 501, 504, 506]:
                                if is_crawl_delay(url):
                                    timeout = sites[o.netloc]["robots"].crawl_delay(
                                        "*") + rate
                                elif rate is not None:
                                    timeout = rate
                                else:
                                    timeout = 10
                                try:
                                    timeout = timeout + rate
                                    int(response.headers["Retry-After"])
                                except:
                                    pass
                                if timeout != 0:
                                    await sleep(timeout)
                                raise aiohttp.ClientResponseError()
                            else:
                                if sites[o.netloc]["Lock"].locked():
                                    sites[o.netloc]["Lock"].release()
                                co = FakeReqest()
                                await co.create(response)
                                await CacheStore(caching_hard, url, response)
                                sites[o.netloc]["timeout"] = time.time()
                                return co
                    except:
                        if sites[o.netloc]["Lock"].locked():
                            sites[o.netloc]["Lock"].release()
                        sites[o.netloc]["timeout"] = time.time()
                        return None

cache = {}
# if os.path.isfile('./cache.json'):
#     f = open("./cache.json", "r")
#     data = f.read()
#     try:
#         cache = json.loads(data)
#     except:
#         pass


async def CacheStore(hard, url, response):
    return None
    if not response.status == 200:
        return None
    if hard:
        cache[url] = {
            "version": response.version,
            "status": response.status,
            "ok": response.ok,
            "method": response.method,
            "content_type": response.content_type,
            "charset": response.charset,
            "text": await response.text(),
        }
        # SAVE
        f = open("./cache.json", "w")
        f.write(json.dumps(cache))
        f.close()

    else:
        return None


async def CacheLoad(url):
    return None
    try:
        r = FakeReqest()
        await r.createCashes(cache[url]["text"], cache[url]["status"])
        return r
    except:
        return None


sem = asyncio.Semaphore(1)
sem2 = asyncio.Semaphore(1)


async def rate_sleep(o, timeout):
    t = time.time()
    timeout = (t - sites[o.netloc]["timeout"])+timeout
    if timeout > 0:
        await sleep(timeout)
    sites[o.netloc]["timeout"] = time.time()


async def setup_robot(url):
    async with ClientSession() as client:
        return await __setup_robot__(url, client)

DNS_LOCK = asyncio.Semaphore(value=50)


async def __setup_robot__(url, client):
    async with ClientSession() as client:
        o = urlparse(url)
        if o.scheme == 'mailto':
            return None
        elif o.scheme == '':
            pass
        elif o.scheme == 'http':
            pass
        elif o.scheme == 'https':
            pass
        else:
            return None
        async with DNS_LOCK:
            try:
                if not o.netloc in sites.keys():
                    for i in range(10):
                        try:
                            result = await dns.asyncresolver.resolve(o.netloc)
                            break
                        except:
                            result = None

                if result is None:
                    sites[o.netloc] = {}
                    sites[o.netloc]["DNS"] = False
                    sites[o.netloc]["Lock"] = asyncio.Semaphore(80)
                    return
                else:
                    if not sites[o.netloc]["DNS"]:
                        sites[o.netloc] = {}
                        sites[o.netloc]["DNS"] = False
                        sites[o.netloc]["Lock"] = asyncio.Semaphore(80)
            except:
                sites[o.netloc] = {}
                sites[o.netloc]["DNS"] = False
                sites[o.netloc]["Lock"] = asyncio.Semaphore(80)
                return None
        if not o.netloc in sites.keys():
            rbo_url = urljoin(url, '/robots.txt')
            for i in range(10):
                try:
                    async with client.get(rbo_url) as response:
                        sites[o.netloc] = {"robots": None}
                        sites[o.netloc]["DNS"] = True
                        sites[o.netloc]["timeout"] = 0
                        try:
                            rp = urllib.robotparser.RobotFileParser(rbo_url)
                            if response.status in (401, 403):
                                rp.disallow_all = True
                            elif response.status >= 400 and response.status < 500:
                                rp.allow_all = True
                                sites[o.netloc]["Lock"] = asyncio.Semaphore(80)
                            else:
                                sites[o.netloc]["Lock"] = asyncio.Semaphore(1)
                            rp.parse(await response.text())
                            sites[o.netloc]["robots"] = rp
                        except:
                            sites[o.netloc]["robots"] = None
                            sites[o.netloc]["Lock"] = asyncio.Semaphore(80)
                        return
                except:
                    pass
        else:
            sites[o.netloc]["robots"] = None
            return


async def reqest_saferobot(url, bot=True, rate=0, retry_on_code=[], caching_hard=False):
    print("looking at ", url)
    async with ClientSession() as client:
        ret = await CacheLoad(url)
        if ret is not None:
            print("found in cashe url:", url)
            return ret
        o = urlparse(url)
        if o.scheme == 'mailto':
            return None
        elif o.scheme == '':
            pass
        elif o.scheme == 'http':
            pass
        elif o.scheme == 'https':
            pass
        else:
            return None
        await __setup_robot__(url, client)
        if sites[o.netloc]["robots"] is not None:
            sites[o.netloc]["robots"].can_fetch("*", url)

        if is_crawl_delay(url):
            timeout = sites[o.netloc]["robots"].crawl_delay("*")
            timeout = timeout + rate
        else:
            timeout = rate
        await sites[o.netloc]["Lock"].acquire()
        if timeout != 0:
            await rate_sleep(o, timeout)
        for i in range(10):
            if True:
                try:
                    print("trying  url:", url, " Timeout:", timeout, " count", i)
                    async with client.get(url) as response:
                        print("url:", url, " status:", response.status)
                        if response.status in [404, 401, 451, 410, 408, 510, 508, 501, 511]:
                            if sites[o.netloc]["Lock"].locked():
                                sites[o.netloc]["Lock"].release()
                            co = FakeReqest()
                            await CacheStore(caching_hard, url, response)
                            await co.create(response)
                            sites[o.netloc]["timeout"] = time.time()
                            return co
                        elif response.status in retry_on_code or response.status in [500, 501, 504, 506]:
                            if is_crawl_delay(url):
                                timeout = sites[o.netloc]["robots"].crawl_delay(
                                    "*") + rate
                            elif rate is not None:
                                timeout = rate
                            else:
                                timeout = 10
                            try:
                                timeout = timeout + rate
                                int(response.headers["Retry-After"])
                            except:
                                pass
                            if timeout != 0:
                                await sleep(timeout)
                            raise aiohttp.ClientResponseError()
                        else:
                            if sites[o.netloc]["Lock"].locked():
                                sites[o.netloc]["Lock"].release()
                            co = FakeReqest()
                            await co.create(response)
                            await CacheStore(caching_hard, url, response)
                            sites[o.netloc]["timeout"] = time.time()
                            return co
                except:
                    if sites[o.netloc]["Lock"].locked():
                        sites[o.netloc]["Lock"].release()
                    sites[o.netloc]["timeout"] = time.time()
                    return None


def mtime(url):

    o = urlparse(url)
    if o.netloc not in sites:
        setup_robot(url)
    if sites[o.netloc]["robots"] is not None:
        timeout = sites[o.netloc]["robots"].mtime()
        if timeout is not None:
            return 0
        return timeout
    return 0


def crawl_delay(url, useragent="FeedScaner"):
    o = urlparse(url)
    if sites[o.netloc]["robots"] is not None:
        timeout = sites[o.netloc]["robots"].crawl_delay(useragent)
        if timeout is not None:
            return 0
        return timeout
    return 0


def is_crawl_delay(url, useragent="FeedScaner"):
    o = urlparse(url)
    if sites[o.netloc]["robots"] is None:
        return False
    timeout = sites[o.netloc]["robots"].crawl_delay(useragent)
    if timeout is None:
        return False
    return True


def site_maps(url):
    o = urlparse(url)
    return sites[o.netloc]["robots"].site_maps()


# response = asyncio.run(reqest_saferobot("https://www.bbc.co.uk/"))
# print(response)

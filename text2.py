from asyncio.tasks import sleep
import asyncio
from re import T
from urllib.parse import urljoin, urlparse
import aiohttp
from aiohttp_retry import RetryClient, ExponentialRetry
from aiohttp import ClientSession

from bs4 import BeautifulSoup
import urllib.robotparser
import requests
import time

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


async def reqests_saferobots(urls, bot=True, rate=0, retry_on_code=[]):
    for url in urls:
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
        if not o.netloc in sites.keys() and not o.netloc in URLLookups.keys():
            sites[o.netloc] = {"robots": None}
            try:
                rp = urllib.robotparser.RobotFileParser()
                rbo_url = urljoin(url, '/robots.txt')
                rp.set_url(rbo_url)
                rp.read()
                sites[o.netloc]["robots"] = rp
            except:
                pass
        if sites[o.netloc]["robots"] is not None:
            sites[o.netloc]["robots"].can_fetch("*", url)
        if is_crawl_delay(url):
            timeout = sites[o.netloc]["robots"].crawl_delay("*")
            timeout = timeout + rate
        for i in range(10):
            print(i)
            try:
                async with ClientSession() as client:
                    async with client.get(url) as response:
                            if response.status in [404, 401, 451, 410, 408, 510, 508, 501, 511]:
                                yield response
                            elif response.status in retry_on_code or response.status in [500, 501, 504, 506]:
                                if is_crawl_delay(url):
                                    timeout = sites[o.netloc]["robots"].crawl_delay("*")
                                elif rate is not None:
                                    timeout = rate
                                else:
                                    timeout = 10
                                try:
                                    timeout = timeout + int(response.headers["Retry-After"])
                                except:
                                    pass
                                sleep(timeout)
                                raise aiohttp.ClientResponseError()
                            else:
                                yield response
            except:
                pass

async def reqest_saferobot(url, bot=True, rate=0, retry_on_code=[]):
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
    if not o.netloc in sites.keys() and not o.netloc in URLLookups.keys():
        sites[o.netloc] = {"robots": None}
        try:
            rp = urllib.robotparser.RobotFileParser()
            rbo_url = urljoin(url, '/robots.txt')
            rp.set_url(rbo_url)
            rp.read()
            sites[o.netloc]["robots"] = rp
        except:
            pass

    if sites[o.netloc]["robots"] is not None:
        sites[o.netloc]["robots"].can_fetch("*", url)
    if is_crawl_delay(url):
        timeout = sites[o.netloc]["robots"].crawl_delay("*")
    timeout = timeout + rate
    sleep(timeout)
    for i in range(10):
        print(i)
        try:
            async with ClientSession() as client:
                async with client.get(url) as response:
                        if response.status in [404, 401, 451, 410, 408, 510, 508, 501, 511]:
                            return response
                        elif response.status in retry_on_code or response.status in [500, 501, 504, 506]:
                            if is_crawl_delay(url):
                                timeout = sites[o.netloc]["robots"].crawl_delay("*") + rate
                            elif rate is not None:
                                timeout = rate
                            else:
                                timeout = 10
                            try:
                                timeout = timeout + int(response.headers["Retry-After"])
                            except:
                                pass
                            sleep(timeout)
                            raise aiohttp.ClientResponseError()
                        else:
                            return response
        except:
            pass


def mtime(url):
    o = urlparse(url)
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
    timeout = sites[o.netloc]["robots"].crawl_delay(useragent)
    if timeout is None:
        return False
    return True


def site_maps(url):
    o = urlparse(url)
    return sites[o.netloc]["robots"].site_maps()


response = asyncio.run(reqest_saferobot(
    "https://www.twilio.com/blog/asynchronous-http-requests-in-python-with-aiohttp/aaaaaaaa"))
print(response)

from asyncio.tasks import sleep
from re import T
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import urllib.robotparser
from enlighten import counter
import requests
import time
# import enlighten

# manager = enlighten.get_manager()
# status_bar = manager.status_bar('Starting UP',color='white_on_red',justify=enlighten.Justify.CENTER)

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


def reqest_saferobot_browser(url, page, browser):
    pass


def reqest_saferobot(url,bot = True,rate = 0,retry_on_code = []):
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
        sites[o.netloc] = { "robots": None}
        try:
            rp = urllib.robotparser.RobotFileParser()
            rbo_url = urljoin(url, '/robots.txt')
            rp.set_url(rbo_url)
            rp.read()
            sites[o.netloc]["robots"] = rp
        except:
            pass
    
    if sites[o.netloc][ "robots"] is  not None:
        sites[o.netloc][ "robots"].can_fetch("*", url)
    timeout = crawl_delay(url)
    if timeout is None:
        timeout = rate
    
    for i in range(30):
        print('wating for: '+str(timeout)+" before requests website:" + url)
        time.sleep(timeout)
        #status_bar.update("seding requests:" + url)
        try:
            response = requests.get(url, headers=headers, timeout=(3.05, 27))
            timeout = sites[o.netloc]["robots"].crawl_delay("*")
            print("Done -","code:", response.status_code ,", urk:", url)
            if response.status_code == 429 | response.status_code == 503:
                if is_crawl_delay(url):
                    timeout = sites[o.netloc]["robots"].crawl_delay("*")
                elif rate is  not None:
                    timeout = rate
                else: 
                    timeout =  10
                try:
                    timeout = timeout + int(response.headers["Retry-After"])
                except:
                    pass
                continue
            elif response.status_code in [404, 401, 451, 410, 408, 510, 508, 501, 511]:
                break
            elif response.status_code in retry_on_code or response.status_code in [500, 501, 504, 506]:
                print("ERROR")
                if is_crawl_delay(url):
                    timeout = sites[o.netloc]["robots"].crawl_delay("*")
                elif rate is  not None:
                    timeout = rate
                else: 
                    timeout =  10
                try:
                    timeout = timeout + int(response.headers["Retry-After"])
                except:
                    pass
                raise timeout
            else:
                break
        except:
            timeout = rate + 10

    #status_bar.update("done:" + url)
    return response


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

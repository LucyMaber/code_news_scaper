from logging import NOTSET
import time
from urllib.parse import urlparse
from urllib.parse import parse_qs
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import requests
import enlighten

from uitls.reqest_man import reqest_saferobot
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-GB,en;q=0.5",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "TE": "trailers",
}

# spinner = Spinner(name='scaning feedspot ')
url_f = {}


async def feedSpot(url):
    if url in url_f:
        return [], []
    url_f[url] = 1
    # spinner.update()
    feeds = []
    webs = []
    r = await reqest_saferobot(url, rate=0.45)
    if r is None:
        return [], []
    soup = BeautifulSoup(r.text, 'html.parser')
    for tlink in soup.select("#fsb a.tlink"):
        try:
            parsed_url = urlparse(tlink["href"])
            captured_value = parse_qs(parsed_url.query)["q"]
            feeds.append(captured_value[0].replace("site:", ""))
        except:
            pass

    for ext in soup.select("#fsb a.ext"):
        webs.append(ext["href"])
    for table in soup.select("table.table > tbody a.et-accent-color1"):
        feed, web = feedSpot(urljoin(url, table["href"]))
        feeds = feed + feeds
        web = web + webs
    return feeds, webs


async def feedspot_start():
    print("feedspot_start")
    # spinner.update()
    feeds, webs = await feedSpot("https://blog.feedspot.com/category/")
    print("Done feedspot")
    return feeds

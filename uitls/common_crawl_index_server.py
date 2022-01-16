import asyncio
from urllib.parse import urlparse
from uitls.reqest_man import reqest_saferobot
from requests.models import PreparedRequest
import json

endpoints = [
]


async def setup_common_crawl_index():
    datas = None
    while datas is None:
        datas = await reqest_saferobot("https://index.commoncrawl.org/collinfo.json")
    print(datas)
    for data in datas.json():
        endpoints.append(data["cdx-api"])


def merge_two_dicts(x, y):
    z = x.copy()   # start with keys and values of x
    z.update(y)    # modifies z with keys and values of y
    return z


async def common_crawl_finder_reqeset(url, domains, d=[]):
    rate = 0
    while True:
        reqest = await reqest_saferobot(url, rate=rate, caching_hard=True)
        if reqest is None:
            continue
        elif reqest.status() == 503:
            rate = rate + 0.001
            continue
        break
    texts = reqest.text().split("\n")
    for text in texts:
        if len(text) != 0:
            a = json.loads(text)
            try:
                if int(a["status"]) > 300 and int(a["status"]) not in [500, 501, 504, 506]:
                    continue
            except:
                pass
            else:
                continue
            if a["url"] not in domains:
                domains[a["url"]] = 1
                d.append(a["url"])
    return d


async def common_crawl_finder(url):
    domains = {}
    domain = urlparse(url)
    if domain.netloc == "":
        domain = url
    else:
        domain = domain.netloc
    domain = domain.replace("https://", "")
    domain = domain.replace("http://", "")
    domain = domain.replace("www.", "")
    list_of_reqeset = []
    list_of_reqeset_page = []
    list_of_reqeset_page2 = []
    reqests = []
    for endpoint in endpoints:
        new_params_Pages = {'url': domain, 'output': "json",
                            "showNumPages": "true", "matchType": "domain"}
        req_page = PreparedRequest()
        req_page.prepare_url(endpoint, new_params_Pages)
        list_of_reqeset_page.append(reqest_saferobot(
            req_page.url, rate=5, caching_hard=True))
        for index_reqest in await asyncio.gather(*list_of_reqeset_page):
            list_of_reqeset_page2.append(index_reqest.json())
        for page_f in list_of_reqeset_page2:
            for pageNum in (range(page_f["pages"])):
                new_params = {'url': domain, 'output': "json",
                              "page": pageNum, "matchType": "domain"}
                req = PreparedRequest()
                req.prepare_url(endpoint, new_params)
                rate = 0
                while True:
                    reqest = await reqest_saferobot(req.url, rate=rate, caching_hard=True)
                    reqests.append(common_crawl_finder_reqeset(reqest.url))
    for index_reqest in await asyncio.gather(*reqests):
        list_of_reqeset = list_of_reqeset + index_reqest
    return list_of_reqeset

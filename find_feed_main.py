import threading
from uitls.blog_feedspot_scraper import feedspot_start
from uitls.common_crawl_index_server import common_crawl_finder, setup_common_crawl_index
from uitls.feed_crawlers import WebStiteScrapeFeed
from uitls.SPRQL import SPRQL, SPARQL_news
import asyncio
from uitls.reddit import reddit_feed_top_domain
import concurrent.futures

loop = asyncio.get_event_loop()


async def sprql():
    print("get WIKIDATA")
    sprql = SPRQL(SPARQL_news, "https://query.wikidata.org/sparql")
    da = sprql.run()
    ret = {}
    async for dakey in da:
        print(da[dakey]["ThingLabel"][0])
        if da[dakey]["ThingLabel"][0] not in ret.keys():
            ret[da[dakey]["ThingLabel"][0]] = {}
        for prop_name in da[dakey].keys():
            if prop_name in ret[da[dakey]["ThingLabel"][0]].keys():
                ret[da[dakey]["ThingLabel"][0]][prop_name] = []
            for i in da[dakey][prop_name]:
                ret[da[dakey]["ThingLabel"][0]][prop_name].append(i)
        print(ret)


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield dict(lst.items()[i:i + n])


async def GEN_main():
    await setup_common_crawl_index()
    reddit = []
    # SPRQL get list of website
    sprql = SPRQL(SPARQL_news, "https://query.wikidata.org/sparql")
    da = sprql.run()
    alist = []
    feedspot = []
    # feedspot = asyncio.create_task(feedspot_start())
    for dakey in da:
        alist.append(asyncio.create_task(
            GEN_core(da, dakey, feedspot, reddit)))
    await asyncio.wait(alist)


def GEN_Thread(da, dakey, feedspot, reddit):
    loop = asyncio.get_event_loop()
    s = loop.run_until_complete(GEN_core(da, dakey, feedspot, reddit))
    x = threading.Thread(target=GEN_Thread,
                         args=(da, dakey, feedspot, reddit))


async def GEN_core(da, dakey, feedspot, reddit):
    # spinner_Feed.update()
    da[dakey]["crawler"] = []
    da[dakey]["page_url"] = []
    da[dakey]["common_crawl"] = []

    finder_cwar = []
    Scrapes = []
    for url in da[dakey]["official_website"]:
        da[dakey]["common_crawl"].append(
            asyncio.create_task(common_crawl_finder(url)))
    if "web_feed_URL" not in da[dakey].keys():
        codeScrape = WebStiteScrapeFeed(da[dakey], 3, feedspot)
        Scrapes.append(codeScrape.crawler())
    await asyncio.gather(*Scrapes)


loop = asyncio.get_event_loop()
s = loop.run_until_complete(GEN_main())

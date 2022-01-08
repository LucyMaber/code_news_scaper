from urllib.parse import urlparse
import tldextract
from uitls.Code_Gen import CodeGen
from uitls.blog_feedspot_scraper import feedspot_start
from uitls.common_crawl_index_server import common_crawl_finder
from uitls.enlightenPlus.cache import Cache
from uitls.feed_crawlers import WebStiteScrapeFeed
from uitls.SPRQL import SPRQL, SPARQL_news
import settings
import asyncpraw
import asyncio
import enlighten
import aiohttp

# from  uitls.enlightenPlus.Spiner import Spinner
# spinnerReddit = Spinner(name="find Reddit")
# spinner_Feed = Spinner(name="find Feed URL")
from uitls.reddit import reddit_feed_top_domain
# web_feed_URL


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


async def GEN_main():
    feeds = []
    # feeds, webs = await feedspot_start()
    # SPRQL
    sprql = SPRQL(SPARQL_news, "https://query.wikidata.org/sparql")
    da = sprql.run()
    # REDDIT
    async with asyncpraw.Reddit(client_id=settings.reddit_client_id, client_secret=settings.reddit_client_secret, user_agent=settings.reddit_user_agent) as reddit:
            alist = []
            for dakey in da:
                alist.append(GEN_core(da, dakey, feeds, reddit))
            await asyncio.gather(*alist)


async def GEN_core(da, dakey, feeds, reddit):
    # spinner_Feed.update()
    da[dakey]["crawler"] = []
    da[dakey]["page_url"] = []
    reddit_lists = []
    finder_cwar = []
    for url in da[dakey]["official_website"]:
        reddit_lists.append(reddit_feed_top_domain(url, reddit))
        finder_cwar.append(common_crawl_finder(url))
    cat = await asyncio.gather(*reddit_lists)
    for reddit_list in  cat:
        for temp in reddit_list:
            da[dakey]["page_url"].append(temp["url"])
    for finder_cwar in await asyncio.gather(*finder_cwar):
        for temp in finder_cwar:
            print(temp)

    da[dakey]["page_url"] = da[dakey]["page_url"] + finder_cwar

    if "web_feed_URL" not in da[dakey].keys():
        da[dakey]["web_feed_URL"] = []

        # SCAN THE WEB SITE FOR MORE FEEDs
    code = WebStiteScrapeFeed(da[dakey], 4)
    await code.crawler(client_http)
    # da[dakey]["crawler"].append()
    print("geting reults crawlers ")
    # GEN THE CODE
    code = CodeGen(da[dakey])
    code.gen_article_article()


# asyncio.run(GEN ())
s = asyncio.run(GEN_main())
print(s)

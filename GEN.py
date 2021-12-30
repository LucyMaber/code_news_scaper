from urllib.parse import urlparse
import tldextract
from uitls.Code_Gen import CodeGen
from uitls.blog_feedspot_scraper import feedspot_start
from uitls.common_crawl_index_server import finder
from uitls.enlightenPlus.cache import Cache
from uitls.feed_crawlers import WebStiteScrapeFeed
from uitls.SPRQL import SPRQL, SPARQL_news
import asyncio
import enlighten
# from  uitls.enlightenPlus.Spiner import Spinner
# spinnerReddit = Spinner(name="find Reddit")
# spinner_Feed = Spinner(name="find Feed URL")
from uitls.reddit import reddit_feed_top_domain
# web_feed_URL
async def sprql ():
  print("get WIKIDATA")
  sprql = SPRQL(SPARQL_news,"https://query.wikidata.org/sparql")
  da = sprql.run()


async def GEN ():
  feeds , webs = await feedspot_start()
  sprql = SPRQL(SPARQL_news,"https://query.wikidata.org/sparql")
  da = sprql.run()
  pbar = enlighten.Counter(total=len(da), desc="geting reults crawlers" , unit='ticks')
  for dakey in da:
    pbar.update()
    # spinner_Feed.update()
    da[dakey]["crawler"] = []
    page_url = []
    for url in da[dakey]["official_website"]:
      #scan REDDIT AND COMMON_CRAWL_INDEX_SERVER
      reddit_list = reddit_feed_top_domain(url)
      pbar_reddit = enlighten.Counter(total=len(reddit_list), desc="reddit" , unit='ticks')
      for temp in  reddit_list:
        pbar_reddit.update()
        page_url.append(temp["url"])
      temp_s =finder(url)
      pbar_s_finder= enlighten.Counter(total=len(temp_s), desc="exter URL" , unit='ticks')
      for temp in  temp_s:
        pbar_s_finder.update()
        page_url= page_url + [temp["url"]]
      o_official_website =  tldextract.extract(url)

      # ADD feed URLS form WIKIDATA and feedspot
      
      pbar_s_feeds = enlighten.Counter(total=len(feeds), desc="exter feeds" , unit='ticks')
      for feed in feeds:
        pbar_s_feeds.update()
        o_feed =  tldextract.extract(url)
        if "web_feed_URL" not in da[dakey].keys():
          da[dakey]["web_feed_URL"]  = []
        if  o_feed.domain  == o_official_website.domain:
          da[dakey]["web_feed_URL"].append(feed)
      if "web_feed_URL" in da[dakey].keys():
        feed = da[dakey]["web_feed_URL"]
      pbar_s_feeds.close()
      
      # SCAN THE WEB SITE FOR MORE FEEDs
      code = WebStiteScrapeFeed(url, 4, page_url)
      da[dakey]["crawler"].append(await code.crawler())
  print("geting reults crawlers ")
  pbar_da = enlighten.Counter(total=len(da), desc="geting reults crawlers" , unit='ticks')
  for dakey in da:
    pbar_da.update()
    for dakey_feed in da[dakey]["crawler"]:
      pass
    code = CodeGen(da[dakey]["official_website"],da[dakey]["web_feed_URL"])
    code.gen_article_article()    
  pbar_s_finder.close()
  pbar_reddit.close()
  pbar_s_feeds.close()
  pbar_da.close()

    
asyncio.run(GEN ())
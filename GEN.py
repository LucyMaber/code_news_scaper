from uitls.Code_Gen import CodeGen
from uitls.feed_crawlers import WebStiteScrapeFeed
from uitls.SPRQL import SPRQL, SPARQL_news
import asyncio
from tqdm import tqdm
# web_feed_URL
async def GEN ():
  sprql = SPRQL(SPARQL_news,"https://query.wikidata.org/sparql")
  da = sprql.run()
  print("setring up crawlers ")
  for dakey in tqdm(da):
    da[dakey]["crawler"] = []
    for i in da[dakey]["official_website"]:
      feed = []
      if "web_feed_URL" in da[dakey].keys():
        feed = da[dakey]["web_feed_URL"]
      code = WebStiteScrapeFeed(i, 2, feed)
      try:
        da[dakey]["crawler"].append(code.crawler())
      except:
        pass
  print("geting reults crawlers ")
  for dakey in tqdm(da):
    print(da[dakey]["crawler"])
    
asyncio.run(GEN ())
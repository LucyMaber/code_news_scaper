import requests

uk_orgs = """
SELECT ?item ?itemLabel ?official_website ?end_time WHERE {
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
  { ?item wdt:P135 ?movement. }
  UNION
  { ?item wdt:P101 ?field_of_work. }
  UNION
  { ?item wdt:P2650 ?interested_in. }
  UNION
  { ?item wdt:P31 wd:Q43229. }
  UNION
  { ?item wdt:P31 wd:Q48204. }
  UNION
  { ?item wdt:P31 wd:Q163740. }
  UNION
  { ?item wdt:P1454 wd:Q240625. }
  UNION
  { ?item wdt:P31 wd:Q1077064. }
  UNION
  { ?item wdt:P1454 wd:Q108514063. }
  UNION
  { ?item wdt:P1454 wd:Q20014246. }
  UNION
  { ?item wdt:P3095 wd:Q25048281. }
  UNION
  { ?item wdt:P1454 wd:Q31273043. }
  UNION
  { ?item wdt:P1454 wd:Q57655560. }
  UNION
  { ?item wdt:P31 wd:Q7188. }
  UNION
  { ?item wdt:P31 wd:Q31728. }
  UNION
  { ?item wdt:P31 wd:Q41298. }
  UNION
  { ?item wdt:P31 wd:Q157031. }
  UNION
  { ?item wdt:P31 wd:Q178790. }
  UNION
  { ?item wdt:P31 wd:Q192350. }
  UNION
  { ?item wdt:P5137 wd:Q185359. }
  UNION
  { ?item wdt:P31 wd:Q210167. }
  UNION
  { ?item wdt:P31 wd:Q216107. }
  UNION
  { ?item wdt:P31 wd:Q219577. }
  UNION
  { ?item wdt:P31 wd:Q206361. }
  UNION
  { ?item wdt:P31 wd:Q38723. }
  UNION
  { ?item wdt:P31 wd:Q7278. }
  UNION
  { ?item wdt:P31 wd:Q929651. }
  UNION
  { ?item wdt:P31 wd:Q431603. }
  UNION
  {?item wdt:P31 wd:Q1666019.}
  ?item wdt:P17 wd:Q145.
  { ?item wdt:P856 ?official_website. }
  MINUS { ?item wdt:P582 ?end_time. }
}
"""

data = """
Q= {Q}
URL =[{URL}]
RSS = [{RSS}]
"""

header={
"accept": 'text/html,application/xhtml+xml',
"accept-encoding" : 'gzip, deflate, br',
"accept-language": 'en-GB,en-US;q=0.9,en;q=0.8',
"sec-ch-ua-mobile": "?0",
"sec-ch-ua-platform": "Linux",
"sec-fetch-dest": "document",
"sec-fetch-mode": "navigate",
"sec-fetch-site": "same-origin",
"sec-fetch-user": "?1",
"upgrade-insecure-requests": "1",
'User-Agent': 'Mozilla/5.0'
}
import re
from bs4 import BeautifulSoup

import asyncio
# from pyppeteer import launch


def checkwebsite(url):
  feed = []
  isgood = False
  try:
    r = requests.get(url["value"],headers=header)
  except:
    pass
    return (False,"" ,"")
  lowertext = r.text.lower()
  for testString in ["news","story","newsletters","articles","rss","newsletter","read more"]:
    if testString in lowertext:
      isgood = True
  soup = BeautifulSoup(r.text, 'html.parser')
  for s in soup.select('a[type="application/rss+xml"]'):
    isgood = True
    feed.append(s['href'])
  for s in soup.select('a[type="application/atom+xml"]'):
    isgood = True
    feed.append(s['href'])
  for testString in ["news","story","newsletters","articles","Articles","rss","newsletter"]:
    for s in soup.findAll(text=re.compile(testString, re.I)):
      isgood = True
  return (isgood,r.url ,feed)
orgs = {}

def main():
  url = 'https://query.wikidata.org/sparql'
  r = requests.get(url, params = {'format': 'json', 'query': uk_orgs})
  data = r.json()
  for i in data["results"]["bindings"]:
    try:
      check = checkwebsite(i["official_website"]) 
      if check[0]:
        orgs[i["itemLabel"]["value"]] = {
          "Q": i["itemLabel"]["item"],
          "URL": check[1],
          "feed": check[2]
        }
    except:
      pass
  

main()

Q ='[[wikidata:Q1900699]]'
urls = [
    "https://www.thenational.scot/"
]
feeds = [
    "https://www.thenational.scot/news/rss/",
    "https://www.thenational.scot/news/scottish-independence/rss/",
    "https://www.thenational.scot/news/fact-check/rss/",
    "https://www.thenational.scot/news/scottish-economy/rss/",
    "https://www.thenational.scot/news/climate-change/rss/",
    "https://www.thenational.scot/news/world/rss/",
    "https://www.thenational.scot/news/science-and-technology/rss/",
    "https://www.thenational.scot/news/coronavirus/rss/",
    "https://www.thenational.scot/politics/snp/rss/",
    "https://www.thenational.scot/politics/nicola-sturgeon/rss/",
    "https://www.thenational.scot/politics/scottish-greens/rss/",
    "https://www.thenational.scot/politics/thejouker/rss/",
    "https://www.thenational.scot/politics/fmqs/rss/",
    "https://www.thenational.scot/politics/labour/rss/",
    "https://www.thenational.scot/politics/conservatives/rss/",
    "https://www.thenational.scot/politics/alba/rss/",
    "https://www.thenational.scot/politics/holyrood/rss/",
    "https://www.thenational.scot/culture/history/rss/",
    "https://www.thenational.scot/news/national/rss/",
    "https://www.thenational.scot/news/national/uk-today/rss/",
    "https://www.thenational.scot/news/national/uk-today/rss/",
    "https://www.thenational.scot/news/national/scotland-today/rss/",

]
header={
    'sec-ch-ua': 'Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': 'Linux',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
}


from bs4 import BeautifulSoup
import requests

def article(url):
    content = requests.get(url,headers=header).content
    soup = BeautifulSoup(content, 'html.parser')
    headline =  soup.select('.headline ')[0]
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('img'):
        s.extract()
    for s in soup.select('#subscription-content > :not(p)'):
        s.extract()
    for s in soup.select('#subscription-content > :contains("READ MORE")'):
        s.extract()
    for s in soup.select('#ayl-wrapper'):
        s.extract()
    content =  soup.select('.article-body')[0]
    
async def scan():
    return False
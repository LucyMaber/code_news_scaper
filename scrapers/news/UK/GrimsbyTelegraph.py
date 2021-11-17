Q ='[[wikidata:Q5609324]]'
urls = [
    "https://www.grimsbytelegraph.co.uk/"
]
feeds = [
"https://www.business-live.co.uk/all-about/yorkshire-humber/?service=rss",
"https://www.grimsbytelegraph.co.uk/all-about/crime/?service=rss",
"https://www.grimsbytelegraph.co.uk/all-about/politics/?service=rss",
"https://www.grimsbytelegraph.co.uk/news/property/?service=rss",
"https://www.grimsbytelegraph.co.uk/all-about/traffic-travel/?service=rss",
"https://www.grimsbytelegraph.co.uk/news/nostalgia/?service=rss",
"https://www.grimsbytelegraph.co.uk/news/uk-world-news/?service=rss",
"https://www.grimsbytelegraph.co.uk/news/?service=rss",
"https://www.grimsbytelegraph.co.uk/news/grimsby-news/?service=rss",
"https://www.grimsbytelegraph.co.uk/all-about/cleethorpes/?service=rss",
"https://www.grimsbytelegraph.co.uk/all-about/scunthorpe/?service=rss",
"https://www.grimsbytelegraph.co.uk/all-about/waltham/?service=rss",
"https://www.grimsbytelegraph.co.uk/all-about/barrow/?service=rss",
"https://www.grimsbytelegraph.co.uk/all-about/barnetby/?service=rss",
"https://www.grimsbytelegraph.co.uk/all-about/utterby/?service=rss",
"https://www.grimsbytelegraph.co.uk/all-about/ulceby/?service=rss",
"https://www.grimsbytelegraph.co.uk/all-about/tetney/?service=rss",
"https://www.grimsbytelegraph.co.uk/all-about/sutton-on-sea/?service=rss",
"https://www.grimsbytelegraph.co.uk/all-about/stallingborough/?service=rss",
"https://www.grimsbytelegraph.co.uk/all-about/south-killingholme/?service=rss",
"https://www.grimsbytelegraph.co.uk/all-about/scartho/?service=rss",
"https://www.grimsbytelegraph.co.uk/all-about/north-thoresby/?service=rss",
"https://www.grimsbytelegraph.co.uk/all-about/north-somercotes/?service=rss",
"https://www.grimsbytelegraph.co.uk/all-about/north-killingholme/?service=rss",
"https://www.grimsbytelegraph.co.uk/all-about/north-cotes/?service=rss",
"https://www.grimsbytelegraph.co.uk/all-about/new-waltham/?service=rss",
"https://www.grimsbytelegraph.co.uk/all-about/new-holland/?service=rss",
"https://www.grimsbytelegraph.co.uk/all-about/marshchapel/?service=rss",
"https://www.grimsbytelegraph.co.uk/all-about/market-rasen/?service=rss",
"https://www.grimsbytelegraph.co.uk/all-about/mablethorpe/?service=rss",
"https://www.grimsbytelegraph.co.uk/all-about/louth/?service=rss",
"https://www.grimsbytelegraph.co.uk/all-about/laceby/?service=rss",
"https://www.grimsbytelegraph.co.uk/all-about/kirmington/?service=rss",
"https://www.grimsbytelegraph.co.uk/all-about/keelby/?service=rss",
"https://www.grimsbytelegraph.co.uk/all-about/ingoldmells/?service=rss",
"https://www.grimsbytelegraph.co.uk/all-about/immingham/?service=rss",
"https://www.grimsbytelegraph.co.uk/all-about/humberston/?service=rss",
"https://www.grimsbytelegraph.co.uk/all-about/holton-le-clay/?service=rss",
"https://www.grimsbytelegraph.co.uk/all-about/healing/?service=rss",
"https://www.grimsbytelegraph.co.uk/all-about/grimsby/?service=rss",
"https://www.grimsbytelegraph.co.uk/all-about/great-limber/?service=rss",
"https://www.grimsbytelegraph.co.uk/all-about/great-coates/?service=rss",
"https://www.grimsbytelegraph.co.uk/all-about/grainthorpe/?service=rss",
"https://www.grimsbytelegraph.co.uk/all-about/goxhill/?service=rss",
"https://www.grimsbytelegraph.co.uk/all-about/freeman-street/?service=rss",
"https://www.grimsbytelegraph.co.uk/all-about/fotherby/?service=rss",
"https://www.grimsbytelegraph.co.uk/all-about/east-ravendale/?service=rss",
"https://www.grimsbytelegraph.co.uk/all-about/east-halton/?service=rss",
"https://www.grimsbytelegraph.co.uk/all-about/cleethorpes/?service=rss",
"https://www.grimsbytelegraph.co.uk/all-about/caistor/?service=rss",
"https://www.grimsbytelegraph.co.uk/all-about/brigg/?service=rss",
"https://www.grimsbytelegraph.co.uk/all-about/binbrook/?service=rss",
"https://www.grimsbytelegraph.co.uk/all-about/barton/?service=rss",
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
    headline =  soup.select('[itemprop="headline name"]')[0]
    description =  soup.select('[itemprop="description"]')[0]
    date_published =  soup.select('.date-published')[0]
    author =  soup.select('.author > a')[0]
    # tags =  soup.select('.tags')[0]
    # datePublished =  soup.select('.datePublished > time')[0]
    # datePublished =  soup.select('.dateModified > time')[0]
    # tags =  soup.select('.tags')[0]
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('.bodytext > :not(ul ,p, strong)'):
        s.extract()
    for s in soup.select('[itemprop="articleBody"] > :not(p)'):
        s.extract()
    content =  soup.select('[itemprop="articleBody"]')[0]
    
async def scan():
    return False

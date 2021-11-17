Q ='[[wikidata:Q5298850]]'
urls = [
    "https://www.dorsetecho.co.uk/"
]
feeds = [
    "https://www.dorsetecho.co.uk/news/rss/",
    "https://www.dorsetecho.co.uk/news/localnews/dorchester/rss/",
    "https://www.dorsetecho.co.uk/sport/rss/",
    "https://www.dorsetecho.co.uk/news/localnews/portland/rss/",
    "https://www.dorsetecho.co.uk/news/localnews/purbeck/rss/",
    "https://www.dorsetecho.co.uk/news/localnews/ourview/rss/",
    "https://www.dorsetecho.co.uk/news/localnews/purbeck/rss/",
    "https://www.dorsetecho.co.uk/news/localnews/ourview/rss/",
    "https://www.dorsetecho.co.uk/news/features/echo_country/rss/",
    "https://www.dorsetecho.co.uk/news/features/lookingback/rss/",
    "https://www.dorsetecho.co.uk/news/features/nostalgia/rss/",
    "https://www.dorsetecho.co.uk/news/features/churchnews/rss/",
    "https://www.dorsetecho.co.uk/news/court/rss/",
    "https://www.dorsetecho.co.uk/news/national/rss/",
    "https://www.dorsetecho.co.uk/news/national/uk-today/rss/",
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
    headline =  soup.select('#article > .headline')[0]
    author =  soup.select('.author-name')[0]
    #subheadline =  soup.select('article > h2 ')[0]
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('#subscription-content > div'):
        s.extract()
    for s in soup.select('#subscription-content > div'):
        s.extract()
    for s in soup.select('#subscription-content > ul'):
        s.extract()
    for s in soup.select('#subscription-content > img'):
        s.extract()
    bodyCopy =  soup.select('.p402_hide')[0]
    
async def scan():
    return False
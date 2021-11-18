Q ='[[wikidata:Q19573385]]'
urls = [
    "https://www.northwaleschronicle.co.uk/"
]
feeds = [
    "https://www.northwaleschronicle.co.uk/news/rss/",
    "https://www.northwaleschronicle.co.uk/news/anglesey/rss/",
    "https://www.northwaleschronicle.co.uk/news/bangor/rss/",
    "https://www.northwaleschronicle.co.uk/news/caernarfon/rss/",
    "https://www.northwaleschronicle.co.uk/news/midgwynedd/rss/",
    "https://www.northwaleschronicle.co.uk/news/crime/news/rss/",
    "https://www.northwaleschronicle.co.uk/news/business/rss/",
    "https://www.northwaleschronicle.co.uk/news/health/rss/",
    "https://www.northwaleschronicle.co.uk/news/general-election/rss/",
    "https://www.northwaleschronicle.co.uk/news/coronavirus/rss/",
    "https://www.northwaleschronicle.co.uk/news/llynpeninsula/rss/",
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
    headline =  soup.select('h1.headline ')[0]
    #subheadline =  soup.select('article > h2')[0]
    for s in soup.select('.p402_hide > :not(p)'):
        s.extract()
    for s in soup.select('img'):
        s.extract()
    bodyCopy =  soup.select('.p402_hide')[0] ### READ THE FULL STORY
    
async def scan():
    return False
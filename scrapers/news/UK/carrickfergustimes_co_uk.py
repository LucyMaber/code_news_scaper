Q ='[[wikidata:Q5046159]]'
urls = [
    "https://www.carrickfergustimes.co.uk/"
]
feeds = [
    "https://www.carrickfergustimes.co.uk/rss"
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
    hedding =  soup.select('article > h1')[0]
    subhedding =  soup.select('article > h2')[0]
    tags =  soup.select('.article-tag') [0]
    for s in soup.select('#content-wrapper > div:not(.markup)'):
        s.extract()
    for s in soup.select('#content-wrapper > aside'):
        s.extract()
    # for s in soup.select('#content-wrapper > #axate-wallet'):
    #     s.extract()
    articleBody  =  soup.select('#content-wrapper') [0]
    #
    
    

async def scan():
    return False
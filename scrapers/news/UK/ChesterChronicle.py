Q ='[[wikidata:Q1070685]]'
urls = [
    "https://www.cheshire-live.co.uk/"
]
feeds = [
    "https://www.cheshire-live.co.uk/news/rss.xml"
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
    #subhedding =  soup.select('article > h2')[0]
    #tags =  soup.select('.article-tag') [0]
    #time =  soup.select('article > time') [0]
    article_headline  =  soup.select('article > h1') [0]
    for s in soup.select('#content-wrapper > div:not(.markup)'):
        s.extract()
    for s in soup.select('#content-wrapper > aside'):
        s.extract()
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('reach-mpu'):
        s.extract()
    for s in soup.select('reach-adyoulike'):
        s.extract()
    for s in soup.select('section'):
        s.extract()
    for s in soup.select('aside'):
        s.extract()
    for s in soup.select('reach-taboola'):
        s.extract()
    for s in soup.select('reach-converse'):
        s.extract()
    for s in soup.select('reach-adyoulike'):
        s.extract()
    for s in soup.select('aside'):
        s.extract()
    for s in soup.select('p:has(b)'):
        s.extract()
    # for s in soup.select('#content-wrapper > #axate-wallet'):
    #     s.extract()
    articleBody  =  soup.select('.article-body') [0]
    #
    

async def scan():
    return False
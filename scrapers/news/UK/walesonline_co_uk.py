Q ='[[wikidata:Q2075898]]'
urls = [
    "https://www.walesonline.co.uk/"
]
feeds = [
    "https://www.walesonline.co.uk/rss.xml"
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
    subheadline =  soup.select('[itemprop="description"]')[0]
    # for s in soup.select('.article-wrapper > :not(p,b,h1,h2,h3,h4,h5,h6,strong)'):
    #     s.extract()
    for s in soup.select('[itemprop="articleBody"] > :not(p,h1,h2,h3,h4,h5,h6) '):
        s.extract()
    for s in soup.select('script'):
        s.extract()
    article =  soup.select('[itemprop="articleBody"]')[0]
    
async def scan():
    return False
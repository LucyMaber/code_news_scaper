Q ='Q100280515'
urls = [
    "https://www.business-live.co.uk/"
]
feeds = [
    "https://www.business-live.co.uk/rss.xml",
    "https://www.business-live.co.uk/all-about/south-west/?service=rss",
    "https://www.business-live.co.uk/all-about/north-west/?service=rss",
    "https://www.business-live.co.uk/all-about/northern-ireland/?service=rss",
    "https://www.business-live.co.uk/all-about/london/?service=rss",
    "https://www.business-live.co.uk/all-about/east/?service=rss",
    "https://www.business-live.co.uk/all-about/yorkshire-humber/?service=rss",
    "https://www.business-live.co.uk/all-about/east-midlands/?service=rss",
    "https://www.business-live.co.uk/all-about/west-midlands/?service=rss",
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
    headline =  soup.select('[itemprop="headline name"]')
    #subheadline =  soup.select('article > h2')
    #for s in soup.select('#content-wrapper >div:not(.markup)'):
    #    s.extract()
    for s in soup.select('.ad-placeholder'):
        s.extract()
    for s in soup.select('[itemprop="articleBody"] > section'):
        s.extract()
    for s in soup.select('[itemprop="articleBody"] > h3'):
        s.extract()
    article_body =  soup.select_one('[itemprop="articleBody"]')
    
async def scan():
    return False
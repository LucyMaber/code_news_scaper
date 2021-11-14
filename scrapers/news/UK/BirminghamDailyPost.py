urls = [
    "https://www.business-live.co.uk/"
]
feeds = [

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
    
article("https://www.business-live.co.uk/manufacturing/computer-chip-shortage-continues-hit-22032800")
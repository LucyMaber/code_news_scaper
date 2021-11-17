Q =''
urls = [
    "https://unherd.com/"
]
feeds = [
    "https://unherd.com/feed/"
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
    headline =  soup.select('h1.entry-title')[0]
    subheadline =  soup.select('.metabox > h4')[0]
    # time =  soup.select('#native-content-pub-date')[0]
    for s in soup.select('img'):
        s.extract()
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('figure'):
        s.extract()
    for s in soup.select('div.article-body.container-fluid > div > div.col-sm-9.col-lg-6 > :not(div > p , p)'):
        s.extract()
    bodyCopy =  soup.select('div.article-body.container-fluid > div > div.col-sm-9.col-lg-6')[0]
    
async def scan():
    return False
Q =''
urls = [
    "https://www.thecanary.co/"
]
feeds = [
    "https://www.thecanary.co/feed/"
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
    headline =  soup.select('[itemprop="name"]')[0]
    #summary =  soup.select('header > .summary')[0]
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('img'):
        s.extract()
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('iframe'):
        s.extract()
    for s in soup.select('[itemprop="articleBody"] > :not(p,h1,h2,h3,h4,h5)'):
        s.extract()
    bodyCopy = soup.select('[itemprop="articleBody"]')[0]
    
async def scan():
    return False
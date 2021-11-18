Q ="Q105820688"
urls = [
    "https://www.chardandilminsternews.co.uk/"
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
    hedding =  soup.select('article > .headline ')[0]
    for s in soup.select('#subscription-content > :not(p)'):
        s.extract()
    articleBody  =  soup.select('#subscription-content') [0]
    

async def scan():
    return False
Q =''
urls = [
    "https://www.bathrecitals.com/"
]
feeds = [
    "https://www.bathrecitals.com/feed/"
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
    headline =  soup.select('[itemprop="headline"]')[0]
    datePublished =  soup.select('[itemprop="datePublished"]')[0]
    for s in soup.select('script'):
        s.extract()
    # for s in soup.select('["itemprop="text"] > :not(p,h1,h2,h3,h4,h5,h6,strong)'):
    #     s.extract()
    bodyCopy = soup.select('[itemprop="text"]')[0]
    
async def scan():
    return False## ERROR uninow
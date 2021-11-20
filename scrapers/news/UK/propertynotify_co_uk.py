Q ='Q67079851'
urls = [
    "https://www.propertynotify.co.uk/"
]
feeds = [
    "https://www.propertynotify.co.uk/feed/",
    "https://www.propertynotify.co.uk/news/press-releases/feed/",
    "https://www.propertynotify.co.uk/investment/feed/",
    "https://www.propertynotify.co.uk/tax/feed/",
    "https://www.propertynotify.co.uk/finance/feed/",
    "https://www.propertynotify.co.uk/news/feed/"
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
    headline =  soup.select('.article__title')[0]
    for s in soup.select('img'):
        s.extract()
    for s in soup.select('.article__detail-text > :not(p,h2,h3,h4,h5,h6)'):
        s.extract()
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('.article__detail-text > p:contains("READ MORE")'):
        s.extract()
    bodyCopy =  soup.select('.article__detail-text')[0] ### READ THE FULL STORY
    
async def scan():
    return False

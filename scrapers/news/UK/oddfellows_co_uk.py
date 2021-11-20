Q ='Q70628298'
urls = [
    "https://www.oddfellows.co.uk/"
]
#NOFEED
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
    headline =  soup.select('.main-content > div > h1')[0]
    #subheadline =  soup.select('article > h2')[0]
    for s in soup.select('.subscription-content > :not(p)'):
        s.extract()
    for s in soup.select('#inArticleAd-2'):
        s.extract()
    for s in soup.select('img'):
        s.extract()
    for s in soup.select('.main-content > div :not(p,h2,h3,h4,h5,h6,h2)'):
        s.extract()
    bodyCopy =  soup.select('.main-content > div')[0] ### READ THE FULL STORY
    
async def scan():
    return False

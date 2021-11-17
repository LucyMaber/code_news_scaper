Q ='[[wikidata:Q7231835]]'
urls = [
    "https://www.northsomersettimes.co.uk/"
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
    headline =  soup.select('.entry-title')[0]
    for s in soup.select('img'):
        s.extract()
    for s in soup.select('[class="single-body entry-content typography-copy"] > :not(p,h2,h3,h4,h5,h6)'):
        s.extract()
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('.article__detail-text > p:contains("READ MORE")'):
        s.extract()
    bodyCopy =  soup.select('[class="single-body entry-content typography-copy"]')[0] ### READ THE FULL STORY
    
async def scan():
    return False

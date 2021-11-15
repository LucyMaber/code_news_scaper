Q ='[[wikidata:Q1566255]]'
urls = []
feeds = [
    "https://www.newstatesman.com/feed",
    ""
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
    headline =  soup.select('.c-article-header__title')[0]
    subheadline =  soup.select('.c-article-excerpt')[0]
    for s in soup.select('.c-article-content__container > :not(p)'):
        s.extract()
    bodyCopy =  soup.select('.c-article-content__container')[0] ### READ THE FULL STORY
    
async def scan():
    return False
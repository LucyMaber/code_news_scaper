Q ="Q17018940"
urls = [
    "https://www.richmondandtwickenhamtimes.co.uk/"
]
feeds = [
    "https://www.richmondandtwickenhamtimes.co.uk/news/national/rss/",
    "https://www.richmondandtwickenhamtimes.co.uk/news/coronavirus/rss/",
    "https://www.richmondandtwickenhamtimes.co.uk/news/rss/",
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
    headline =  soup.select('.headline')[0]
    subheadline =  soup.select('[itemprop="description"] ')[0]
    for s in soup.select('img'):
        s.extract()
    for s in soup.select('#subscription-replace-entire-article > :not(p,h2,h3,h4,h5,h6)'):
        s.extract()
    bodyCopy =  soup.select('.article-body ')[0] ### READ THE FULL STORY
    
async def scan():
    return False
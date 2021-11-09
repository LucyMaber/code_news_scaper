urls = [
    "https://www.freepressseries.co.uk/"
]
feeds = [
    "https://www.freepressseries.co.uk/news/rss/"
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
    headline =  soup.select('#article > h1')[0]
    for s in soup.select('img'):
        s.extract()
    for s in soup.select('.p402_hide > :not(p,h2,h3,h4,h5,h6)'):
        s.extract()
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('.p402_hide > p:contains("READ MORE")'):
        s.extract()
    bodyCopy =  soup.select('.article-body')[0] ### READ THE FULL STORY
    print(bodyCopy)
article("https://www.freepressseries.co.uk/news/19457276.court-newport-cwmbran-caerphilly/")
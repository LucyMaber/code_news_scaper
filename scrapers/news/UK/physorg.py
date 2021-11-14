urls = [
    "https://phys.org/"
]
feeds = [
    "https://phys.org/rss-feed/",
    "https://phys.org/rss-feed/breaking/",
    "https://phys.org/rss-feed/editorials/",
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
    headline =  soup.select('article > h1')[0]
    for s in soup.select('.article-main  div'):
        s.extract()
    for s in soup.select('.article-main__explore ~ div'):
        s.extract()
    for s in soup.select('img'):
        s.extract()
    for s in soup.select('hr'):
        s.extract()
    for s in soup.select('.article-main__note'):
        s.extract()
    for s in soup.select('script'):
        s.extract()
    bodyCopy =  soup.select('.article-main')[0] ### READ THE FULL STORY
    
article("https://techxplore.com/news/2021-11-merlin-self-supervised-strategy-deep-despeckling.html")
urls = [
    "https://www.autosport.com/"
]
## ADD more feeds
feeds = [
    "https://www.autosport.com/rss/all/news/",
    "https://www.autosport.com/rss/all/news/",
    "https://www.autosport.com/rss/all/news/",
    "https://www.autosport.com/rss/all/news/",
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
    author =  soup.select('a[rel="author"]') [0]
    print(author)
    co_author =  soup.select('a[rel="author"]') [0]
    print(author)
    time =  soup.select('time.ms-article-header-prime__date_value') [0]
    print(time)
    for s in soup.select("section[contenteditable]"):
        s.extract()
    for s in soup.select("div.ms-article-content > div"):
        s.extract()
    for s in soup.select(".ms-ap-native"):
        s.extract()
    for s in soup.select("#ms-piano_article-prebanner"):
        s.extract()
    for s in soup.select(".ms-entity-detail-header-row"):
        s.extract()
    for s in soup.select("section[contenteditable]"):
        s.extract()
    for s in soup.select("#ms-sponsored-content-bootom-container"):
        s.extract()
    for s in soup.select(".party-poker"):
        s.extract()
    for s in soup.select("#party-poker-tpl"):
        s.extract()
    for s in soup.select(".party-poker"):
        s.extract()
    article =  soup.select('div.ms-article-content') [0]
    print(article)
    subtitle =  soup.select('h2.ms-article_preview') [0]
    print(subtitle)
    ##FIX ME SILL NEED TO REMOVE JUNK
article("https://www.autosport.com/f1/news/williams-f1-walrus-nose-aerodynamicist-terzi-dies/6734186/")
urls = [
    "https://www.yourlocalguardian.co.uk/news/kingstonnews/"
]
feeds = [
    "https://www.yourlocalguardian.co.uk/news/kingstonnews/rss/",
    "https://www.yourlocalguardian.co.uk/news/kingstonnews/rss/"
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
    headline =  soup.select("article > h1")[0]
    time =  soup.select("article > time")[0]
    author =  soup.select(".author-name > a")[0]
    for s in soup.select('script'):
        s.extract()
    bodyCopy =  soup.select("div.p402_hide")[0]
    print(author)
article("https://www.yourlocalguardian.co.uk/news/19691129.chelseas-tuchel-safe-now/")
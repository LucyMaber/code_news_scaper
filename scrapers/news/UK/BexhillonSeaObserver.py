urls = [
    "https://www.bexhillobserver.net/"
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
    headline =  soup.select('article > h1')
    subheadline =  soup.select('article > h2')
    for s in soup.select('#content-wrapper >div:not(.markup)'):
        s.extract()
    for s in soup.select('#content-wrapper >h3'):
        s.extract()
    article_body =  soup.select_one('#content-wrapper')
    print(article_body)
article("https://www.bexhillobserver.net/sport/football/hollingtons-halloween-nightmare-delivery-was-nothing-short-of-atrocious-3439329")
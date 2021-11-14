Q ='[[wikidata:Q1049657]]'
urls = [
    "https://www.scotsman.com/"
]
feeds = [
    "https://www.scotsman.com/rss"
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
    headline =  soup.select('#content-wrapper > h1')[0]
    subheadline =  soup.select('#content-wrapper > h2')[0]
    # time =  soup.select('#native-content-pub-date')[0]
    for s in soup.select('img'):
        s.extract()
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('.article-content > .article-read-more ~ *'):
        s.extract()
    for s in soup.select('.article-content > :not(.markup)'):
        s.extract()
    bodyCopy =  soup.select('.article-content')[0]
    
article("https://www.scotsman.com/sport/football/rangers/aston-villa-confirm-steven-gerrard-appointment-as-he-notes-special-place-in-his-heart-for-rangers-3453857")


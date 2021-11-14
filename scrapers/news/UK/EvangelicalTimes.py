Q ='[[wikidata:Q5415762]]'
urls = [
    "https://www.evangelical-times.org/"
]
feeds = [
    "https://www.evangelical-times.org/feed"
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
    headline =  soup.select('.left > h1')[0]
    tags =  soup.select('.tags')[0]
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('.tags'):
        s.extract()
    for s in soup.select('[style]'):
        s.extract()
    for s in soup.select('.main > div'):
        s.extract()
    for s in soup.select('script'):
        s.extract()
    bodyCopy =  soup.select(".main")[0]
    
article("https://www.evangelical-times.org/articles/as-we-prepare-to-remember/")
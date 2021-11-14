Q ='[[wikidata:Q7741518]]'
urls = [
    "https://www.impartialreporter.com/"
]
feeds = [
    "https://www.impartialreporter.com/news/rss/"
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
    headline =  soup.select('h1.headline')[0]
    for s in soup.select('script'):
        s.extract()
    content =  soup.select('.p402_hide')[0]
    
article("https://www.impartialreporter.com/news/19708222.fermanagh-2001-reflections-ruc-force-enniskillen-ties-end/")

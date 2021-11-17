Q ='[[wikidata:Q7681172]]'
urls = [
    "https://www.questmedianetwork.co.uk/news/tameside-reporter/advice-available-to-families-at-the-healthy-hub-club/"
]
feeds = [
    "https://www.questmedianetwork.co.uk/news/tameside-reporter/feed.xml"
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
    headline =  soup.select('.o-headline')[0]
    time =  soup.select(".news-timestamp")[0]
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('.gm-group >:not(p,h1,h2,h3,h4,h5,h6,strong)'):
        s.extract()
    for s in soup.select('.gm-group >  :contains("Read more from") ~ *'):
        s.extract()
    for s in soup.select('.gm-group >  :contains("Read more from")'):
        s.extract()
    bodyCopy =  soup.select('.gm-group')[0]
    
async def scan():
    return False
Q ='[[wikidata:Q7018146]]'
urls = [
    "https://www.newhamrecorder.co.uk/"
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
    headline =  soup.select('[class="article__title mdc-typography--headline4"]')[0]
    for s in soup.select('[class="article__detail-text mdc-typography--body1"] > :not(p)'):
        s.extract()
    bodyCopy =  soup.select('[class="article__detail-text mdc-typography--body1"]:has(p)')[0]
    
article("https://www.newhamrecorder.co.uk/news/westfield-stratford-city-car-fire-cause-being-investigated-8471470")

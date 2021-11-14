Q ='[[wikidata:Q7639561]]'
urls = [
    "https://www.thesun.co.uk/"
]
feeds = [
    "https://www.thesun.co.uk/feed/"
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
    headline =  soup.select('.article__headline')[0]
    #time =  soup.select("article > time")[0]
    for s in soup.select('script'):
        s.extract() #p
    for s in soup.select('.article__content >  :not(p)'):
        s.extract()
    for s in soup.select('.article__content >  p:contains("for the latest updates")'):
        s.extract()
    for s in soup.select('.article__content >  p:contains(" Read our")'):
        s.extract()
    bodyCopy =  soup.select('.article__content')[0]
    
article("https://www.thesun.co.uk/news/16683232/prince-andrew-virginia-roberts-witness-evidence-documentary/")
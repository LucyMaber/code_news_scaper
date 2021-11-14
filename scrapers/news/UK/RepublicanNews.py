Q ='[[wikidata:Q7314617]]'
urls = [
    "https://www.independent.co.uk/"
]
feeds = [
    "https://www.independent.co.uk/rss"
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
    headline =  soup.select('#articleHeader > div > div > h1')[0]
    subheadline =  soup.select('#articleHeader > div > div > h2')[0]
    for s in soup.select('img'):
        s.extract()
    for s in soup.select('#main> :not(p,h2,h3,h4,h5,h6)'):
        s.extract()
    for s in soup.select('#main> p:contains("READ MORE:")'):
        s.extract()
    for s in soup.select('#main> p:contains("Sign up for our newsletter and get the top stories")'):
        s.extract()
    bodyCopy =  soup.select('#main')[0] ### READ THE FULL STORY
    
article("https://www.independent.co.uk/news/uk/politics/boris-johnson-news-debate-owen-paterson-b1954076.html")

Q ='[[wikidata:Q7300538]]'
urls = [
    "https://www.getreading.co.uk/"
]
feeds = [
    "https://www.getreading.co.uk/rss-feeds/"
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
    headline =  soup.select('[itemprop="headline name"]')[0]
    subheadline =  soup.select('[itemprop="description"]')[0]
    dateModified =  soup.select('[itemprop="dateModified"]')[0]
    for s in soup.select('img'):
        s.extract()
    for s in soup.select('[itemprop="articleBody"] > :not(p,h2,h3,h4,h5,h6)'):
        s.extract()
    for s in soup.select('[itemprop="articleBody"] > p:contains("READ MORE:")'):
        s.extract()
    for s in soup.select('[itemprop="articleBody"] > p:contains("Sign up for our newsletter and get the top stories")'):
        s.extract()
    for s in soup.select('#main> p:contains("To sign up for the Lincolnshire Live newsletter")'):
        s.extract()
    bodyCopy =  soup.select('[itemprop="articleBody"]')[0] ### READ THE FULL STORY
    
article("https://www.getreading.co.uk/news/reading-berkshire-news/wokingham-traffic-plans-direct-link-22068653")
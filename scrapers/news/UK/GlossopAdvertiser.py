Q ='[[wikidata:Q5571937]]'
urls = [
    "https://www.questmedianetwork.co.uk/"
]
feeds = [
    "https://www.questmedianetwork.co.uk/news/glossop-chronicle/feed.xml"
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
    description =  soup.select('.news-abstract')[0]
    # description =  soup.select('h3.entry-title')[0]
    # author =  soup.select('.author > a')[0]
    time =  soup.select('.news-timestamp')[0]
    for s in soup.select('article > :not(p)'):
        s.extract()
    for s in soup.select('.news-abstract'):
        s.extract()
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('p:contains("Click here")'):
        s.extract()
    content =  soup.select('article')[0]
    
article("https://www.questmedianetwork.co.uk/news/glossop-chronicle/staff-from-glossop-charity-join-forces-with-digital-forum/")
Q =''
urls = [
    "https://www.northantstelegraph.co.uk/"
]
feeds = [
    "https://www.northantstelegraph.co.uk/rss"
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
    headline =  soup.select('article > h1')[0]
    description =  soup.select('article > h2')[0]
    for s in soup.select('figure'):
        s.extract()
    for s in soup.select('reach-mpu'):
        s.extract()
    for s in soup.select('reach-adyoulike'):
        s.extract()
    for s in soup.select('section'):
        s.extract()
    for s in soup.select('reach-taboola'):
        s.extract()
    for s in soup.select('reach-converse'):
        s.extract()
    for s in soup.select('reach-adyoulike'):
        s.extract()
    for s in soup.select('.html-embed'):
        s.extract()
    for s in soup.select('p:has(b)'):
        s.extract()
    for s in soup.select('#content-wrapper > p:contains("Read more")'):
        s.extract()
    for s in soup.select('#content-wrapper > :not(.markup)'):
        s.extract()
    articleBody =  soup.select('#content-wrapper')[0]
    
article("https://www.northantstelegraph.co.uk/news/people/a45-chowns-mill-closures-start-tonight-with-more-to-come-3447223")
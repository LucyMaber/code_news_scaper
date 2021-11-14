urls = [
    "https://www.walesonline.co.uk/"
]
feeds = [
    "https://www.walesonline.co.uk/rss.xml"
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
    headline =  soup.select('h1')[0]
    #time =  soup.select('[itemprop="datePublished"]')[0]
    for s in soup.select('script'):
        s.extract()
    # for s in soup.select('#main >:not(p,h1,h2,h3,h4,h5,h6,strong)'):
    #     s.extract() #markup
    for s in soup.select('aside'):
        s.extract()
    for s in soup.select('p:has([data-link-tracking="InArticle|Link"])'):
        s.extract()
    for s in soup.select('span.mor-linkcle'):
        s.extract()
    for s in soup.select('.share-title'):
        s.extract()
    bodyCopy =  soup.select('#main')[0]
    
article("https://www.standard.co.uk/news/uk/uk-travellers-covid-booster-jab-travel-restriction-b964815.html")
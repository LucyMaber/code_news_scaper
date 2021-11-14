Q ='[[wikidata:Q255073]]'
urls = [
    "https://www.joe.co.uk/"
]
feeds = [
    "https://www.joe.co.uk/feed"
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
    headline =  soup.select('.title-section > h1')[0]
    #tags =soup.select('.ArticleCategories__category')[0]
    for s in soup.select('.article-content > :not(p, h1,h2,h3,h4,h5,h6,.twitter-tweet)'):
        s.extract()
    article =  soup.select('.article-content')[0]
    
article("https://www.joe.co.uk/news/man-trapped-in-wall-of-new-york-theatre-for-two-days-completely-naked-298237")

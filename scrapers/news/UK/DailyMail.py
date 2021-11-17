Q ='[[wikidata:Q210534]]'
urls = [
    "https://www.dailymail.co.uk/"
]
feeds = [
    "https://www.dailymail.co.uk/home/index.rss",
    "https://www.dailymail.co.uk/news/articles.rss"
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
    headline =  soup.select('#js-article-text h2')[0]
    discation =  soup.select('.mol-bullets-with-font')[0]
    articleBody =  soup.select('[itemprop="articleBody"]')[0]
    for s in soup.select('[itemprop="articleBody"] > div:not(.mol-para-with-font)'):
        s.extract()
    
async def scan():
    return False
Q ='[[wikidata:Q11148]]'
urls = [
    "https://www.theguardian.com"
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
    headline =  soup.select('article > div > div > div > div > div > h1')[0]
    # tags =  soup.select('.tags')[0]
    # datePublished =  soup.select('.datePublished > time')[0]
    # datePublished =  soup.select('.dateModified > time')[0]
    # tags =  soup.select('.tags')[0]
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('#maincontent > div > :not(ul ,p, strong)'):
        s.extract()
    for s in soup.select('[itemprop="articleBody"] > :not(p)'):
        s.extract()
    content =  soup.select('#maincontent > div')[0]
    
article("https://www.theguardian.com/politics/2021/nov/05/article-16-very-much-on-the-table-in-brexit-row-david-frost")

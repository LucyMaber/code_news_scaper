Q ='[[wikidata:Q16991712]]'
urls = [
    "https://www.surreycomet.co.uk/"
]
feeds = [
    "https://www.surreycomet.co.uk/news/rss/",
    "https://www.surreycomet.co.uk/news/kingston/rss/",
    "https://www.surreycomet.co.uk/news/epsom/rss/",
    "https://www.surreycomet.co.uk/news/coronavirus/rss/",
    "https://www.surreycomet.co.uk/news/national/rss/",
    "https://www.surreycomet.co.uk/news/national/uk-today/rss/",
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
    headline =  soup.select("article > h1")[0]
    by =   soup.select(".job-title")[0]
    datePublished =   soup.select('[itemprop="datePublished"]')[0]
    for s in soup.select('script'):
        s.extract()
    bodyCopy =  soup.select(".p402_hide")[0]
    
async def scan():
    return False
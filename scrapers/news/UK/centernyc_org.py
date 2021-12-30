Q =''
urls = [
    "http://www.centernyc.org/"
]
feeds = [
    "http://www.centernyc.org/home-2?format=rss"
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
    headline =  soup.select('.articleTitle')[0]
    articleDate =  soup.select('#articleDate')[0]
    articleSummary =  soup.select('.articleSummary')[0]
    articleContent  =  soup.select('div.articleSummary > h2 > p ') [0] #
    alter  =  soup.select('#articleName')
    for s in soup.select('.articleContent > div >div > em'):
        s.extract()
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('img'):
        s.extract()
    # for s in soup.select('#content-wrapper > #axate-wallet'):
    #     s.extract()
    articleContent  =  soup.select('.articleContent > div') [0]
    

async def scan():
    return False
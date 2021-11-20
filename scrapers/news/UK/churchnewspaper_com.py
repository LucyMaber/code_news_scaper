Q ='Q5116865'
urls = [
    "https://www.churchnewspaper.com/"
]
feeds = [
"https://www.churchnewspaper.com/feed"
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
    headline =  soup.select('[itemprop="headline"]')[0]
    author =  soup.select('[itemprop="author"]')[0]
    datePublished =  soup.select('[itemprop="datePublished"]')[0]
    article_headline  =  soup.select('[itemprop="text"]') [0]
    for s in soup.select('[itemprop="text"] > div'):
        s.extract()
    # for s in soup.select('#content-wrapper > #axate-wallet'):
    #     s.extract()
    articleBody  =  soup.select('.entry-content') [0]
    #
    

async def scan():
    return False
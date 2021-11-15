Q =''
urls = [
    "https://www.thenews.coop/"
]
feeds = [
    "https://www.thenews.coop/feed/"
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
    # Need to add author
    article_subtitle =  soup.select('[itemprop="description"]')[0]
    article_title =  soup.select('[itemprop="headline"]')[0]
    author_name = soup.select(".author-name > a")[0]
    time =  soup.select(".xt-post-date")[0]
    tags =  soup.select(".article-categories > ul")[0]
    for s in soup.select("script"):
        s.extract()
    for s in soup.select('[itemprop="articleBody"] > div'):
        s.extract()
    entry_content =  soup.select('[itemprop="articleBody"]')[0]
    
async def scan():
    return False
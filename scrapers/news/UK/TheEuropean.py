urls = [
    "https://www.theneweuropean.co.uk/"
]
feeds = [
    "https://www.theneweuropean.co.uk/feed"
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
    headline =  soup.select('[class="ne-article__title"]')[0]
    subheadline =  soup.select('[class="ne-article__excerpt"]')[0]
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('img'):
        s.extract()
    for s in soup.select('main > :not(.ne-article__post-content)'):
        s.extract()
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('iframe'):
        s.extract()
    for s in soup.select('[class="pp-content__body pp-subs pp-subs__post-end"] > :not(p)'):
        s.extract()
    bodyCopy = soup.select('main')[0]
    print(bodyCopy)
article("https://www.theneweuropean.co.uk/jk-rowling-trans-culture-war/")
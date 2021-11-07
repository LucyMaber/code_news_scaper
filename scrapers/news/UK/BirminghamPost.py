urls = [
    "https://www.birminghammail.co.uk/"
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
    headline =  soup.select_one('[itemprop="headline name"]')
    description =  soup.select_one('[itemprop="description"]')
    author =  soup.select_one(".publication-theme")
    published =  soup.select_one("time.date-published")
    updated =  soup.select_one("time.date-updated")
    #subheadline =  soup.select('article > h2')
    #for s in soup.select('#content-wrapper >div:not(.markup)'):
    #    s.extract()
    for s in soup.select('.ad-placeholder'):
        s.extract()
    for s in soup.select('[itemprop="articleBody"] > section'):
        s.extract()
    for s in soup.select('[itemprop="articleBody"] > h3'):
        s.extract()
    for s in soup.select('script'):
        s.extract()
    for s in soup.select("p:has(b)"):
        s.extract()
    article_body =  soup.select_one('[itemprop="articleBody"]')
    print(article_body)
article("https://www.birminghammail.co.uk/news/midlands-news/birmingham-woman-who-stole-childrens-21967614")
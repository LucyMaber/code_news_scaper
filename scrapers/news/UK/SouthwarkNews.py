urls = [
    "https://www.southwarknews.co.uk/"
]
feeds = [
    "https://www.southwarknews.co.uk/news/inner-london-crown-court-to-be-spared-axe-amid-spiralling-criminal-case-backlog/feed/"
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
    headline =  soup.select(' div > div > div.col-8.single-maincol > h1')[0]
    subheadline =  soup.select('div > div > div.col-8.single-maincol > p.intropara')[0]
    # for s in soup.select('.article-wrapper > :not(p,b,h1,h2,h3,h4,h5,h6,strong)'):
    #     s.extract()
    for s in soup.select('#single-article-content > :not(p,h1,h2,h3,h4,h5,h6) '):
        s.extract()
    for s in soup.select('script'):
        s.extract()
    article =  soup.select('#single-article-content')[0]
    print(article)
article("https://www.southwarknews.co.uk/news/inner-london-crown-court-to-be-spared-axe-amid-spiralling-criminal-case-backlog/")
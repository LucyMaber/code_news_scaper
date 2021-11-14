Q ='[[wikidata:Q5132015]]'
urls = [
    "https://www.thewestonmercury.co.uk/"
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
    # Need to add author
    by =  soup.select("p.badge__name")[0]
    article_title =  soup.select("h1.article__title")[0]
    article_published  =  soup.select("div.article__published > div:nth-child(1) > span.mdc-typography--body2")[0]
    article_updated =  soup.select("div.article__published > div:nth-child(2) > span.mdc-typography--body2")[0]
    for s in soup.select(".article__detail-text > div"):
        s.extract()
    article_text  =  soup.select("div.article__detail-text")[0]
    

article("https://www.thewestonmercury.co.uk/news/baytree-school-judicial-review-lodged-8432964")
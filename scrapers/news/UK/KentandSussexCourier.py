urls = [
    "https://www.kentlive.news/"
]
feeds = [
    "https://www.kentlive.news/rss.xml"
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
    try:
        headline =  soup.select('article > h1')[0]
    except:
        headline =  soup.select('[itemprop="headline name"]')[0]
    description =  soup.select('article > .sub-title')[0]
    try:
        dateModified =  soup.select('.date-updated')[0]
    except:
        dateModified =  soup.select('[itemprop="dateModified"]')[0]
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('p:has([data-link-tracking="InArticle|Link"])'):
        s.extract()
    for s in soup.select('.entry-content > :not(p , h1 , h2 , h3 , h4 , h5 , h6 , h7 , h8 , h9 , time)'):
        s.extract()
    for s in soup.select('.entry-content > :not(p , h1 , h2 , h3 , h4 , h5 , h6 , h7 , h8 , h9 , time)'):
        s.extract()
    for s in soup.select('.entry-info > :not(p , h1 , h2 , h3 , h4 , h5 , h6 , h7 , h8 , h9 , time)'):
        s.extract()
    for s in soup.select('.entry-content > :not(p , h1 , h2 , h3 , h4 , h5 , h6 , h7 , h8 , h9 , time)'):
        s.extract()
    for s in soup.select('.entry-content > :not(p , h1 , h2 , h3 , h4 , h5 , h6 , h7 , h8 , h9 , time)'):
        s.extract()
    for s in soup.select('.live-event-lead-entry > :not(p , h1 , h2 , h3 , h4 , h5 , h6 , h7 , h8 , h9 , time)'):
        s.extract()
    for s in soup.select('[itemprop="articleBody"] > :not(p , h1 , h2 , h3 , h4 , h5 , h6 , h7 , h8 , h9 , time)'):
        s.extract()
    artcal =  soup.select('.article-body')[0]
    print(artcal)

article("https://www.kentlive.news/news/uk-world-news/delivery-scams-rise--how-6142803")
urls = [
    "https://www.devonlive.com/"
]
feeds = [
    "https://www.devonlive.com/rss.xml"
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
    headline =      soup.select('[itemprop="headline name"]')[0]
    description =   soup.select('[itemprop="description"]')[0]
    #dateModified =  soup.select('time')[0]
    for s in soup.select('figure'):
        s.extract()
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('p:contains("Want our best stories with fewer ads and alerts? Download our app on ")'):
        s.extract()
    for s in soup.select('p:contains("READ MORE")'):
        s.extract()
    for s in soup.select('p:contains("Read more:")'):
        s.extract()
    for s in soup.select('[itemprop="articleBody"] > div'):
        s.extract()
    for s in soup.select('[data-link-tracking="InArticle|Link"]'):
        s.extract()
    articleBody =  soup.select('[itemprop="articleBody"]')[0]
    
article("https://www.devonlive.com/news/devon-news/pictures-show-quiet-street-heart-6104302")
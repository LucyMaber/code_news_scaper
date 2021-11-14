urls = [
    "https://www.dailystar.co.uk/"
]
feeds = [
    "https://www.dailystar.co.uk/rss.xml"
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
    headline =  soup.select('[itemprop="headline name"]')[0]
    description =  soup.select('[itemprop="description"]')[0]
    dateModified =  soup.select('[itemprop="dateModified"]')[0]
    by =  soup.select('.publication-theme')[0]
    time =  soup.select('.date-published')[0]
    for s in soup.select('.read-more-links'):
        s.extract()
    for s in soup.select('.embedded-image-grid brand-low'):
        s.extract()
    for s in soup.select('.embedded-image-grid'):
        s.extract()
    for s in soup.select('p:has([data-link-tracking="InArticle|Link"])'):
        s.extract()
    for s in soup.select('figcaption'):
        s.extract()
    for s in soup.select('meta'):
        s.extract()
    for s in soup.select('img'):
        s.extract()
    for s in soup.select('figure'):
        s.extract()
    for s in soup.select('reach-mpu'):
        s.extract()
    for s in soup.select('reach-adyoulike'):
        s.extract()
    for s in soup.select('reach-taboola'):
        s.extract()
    for s in soup.select('reach-converse'):
        s.extract()
    for s in soup.select('section'):
        s.extract()
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('reach-adyoulike'):
        s.extract()
    for s in soup.select('.html-embed'):
        s.extract()
    bodyCopy =  soup.select('[itemprop="articleBody"]')[0]
    
article("https://www.dailystar.co.uk/news/world-news/cleo-smith-abduction-suspect-viciously-25372777")

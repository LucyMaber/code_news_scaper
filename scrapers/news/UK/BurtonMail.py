urls = [
    "https://www.staffordshire-live.co.uk/"
]
feeds = [
 "https://www.staffordshire-live.co.uk/rss.xml"
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
    hedding =  soup.select('[itemprop="headline name"]') [0]
    subhedding =  soup.select('[itemprop="description"]') [0]
    publishedTime =  soup.select('.date-published') [0]
    dateModified =  soup.select('[itemprop="dateModified"]') [0]
    by =  soup.select('.author') [0]
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('p:has(b)'):
        s.extract()
    for s in soup.select('figure'):
        s.extract()
    for s in soup.select('reach-mpu'):
        s.extract()
    for s in soup.select('reach-adyoulike'):
        s.extract()
    for s in soup.select('section'):
        s.extract()
    for s in soup.select('reach-taboola'):
        s.extract()
    for s in soup.select('reach-mpu'):
        s.extract()
    for s in soup.select('reach-adyoulike'):
        s.extract()
    for s in soup.select('section'):
        s.extract()
    for s in soup.select('reach-taboola'):
        s.extract()
    for s in soup.select('section'):
        s.extract()
    for s in soup.select('reach-converse'):
        s.extract()
    for s in soup.select('reach-adyoulike'):
        s.extract()
    for s in soup.select('p:has(b)'):
        s.extract()
    articleBody =  soup.select('[itemprop="articleBody"]') [0]
    
article("https://www.staffordshire-live.co.uk/news/local-news/criminals-who-been-locked-up-6143221")
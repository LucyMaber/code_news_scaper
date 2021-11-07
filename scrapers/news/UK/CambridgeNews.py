urls = [
    "https://www.cambridge-news.co.uk/"
]
feeds = [
    "https://www.cambridge-news.co.uk/rss.xml"
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
    hedding =  soup.select('[itemprop="headline name"]')[0]
    subhedding =  soup.select('[itemprop="description"]')[0]
    dateModified =  soup.select('[itemprop="dateModified"]') [0]
    # by =  soup.select('.byline') [0]
    # tags =  soup.select('.article-tag') [0]
    for s in soup.select('[itemprop="articleBody"] > div'):
        s.extract()
    for s in soup.select('[itemprop="articleBody"] > p:has(b)'):
        s.extract()
    for s in soup.select('[itemprop="articleBody"] > figure'):
        s.extract()
    for s in soup.select('[itemprop="articleBody"] > reach-mpu'):
        s.extract()
    for s in soup.select('[itemprop="articleBody"] > reach-adyoulike'):
        s.extract()
    for s in soup.select('[itemprop="articleBody"] > reach-taboola'):
        s.extract()
    for s in soup.select('[itemprop="articleBody"] > reach-converse'):
        s.extract()
    for s in soup.select('[itemprop="articleBody"] > reach-adyoulike'):
        s.extract()
    for s in soup.select('[itemprop="articleBody"] > script'):
        s.extract()
    for s in soup.select('[itemprop="articleBody"] > section'):
        s.extract()
    articleBody  =  soup.select('[itemprop="articleBody"]') [0]
    print(subhedding)

article("https://www.cambridge-news.co.uk/news/cambridge-news/devastated-dad-cambridge-teen-totally-22039696")
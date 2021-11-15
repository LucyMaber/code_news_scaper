Q ='[[wikidata:Q85802013]]'
urls = [
    "https://www.somersetlive.co.uk/"
]
feeds = [
    "https://www.somersetlive.co.uk/rss.xml"
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
    time =  soup.select('.date-published ')[0]
    # for s in soup.select('.article-wrapper > :not(p,b,h1,h2,h3,h4,h5,h6,strong)'):
    #     s.extract()
    for s in soup.select('[itemprop="articleBody"] > :not(p, h1,h2,h3,h4,h5,h6) '):
        s.extract()
    for s in soup.select('[itemprop="articleBody"] > p:contains("READ MORE")'):
        s.extract()
    for s in soup.select('[itemprop="articleBody"] > p:contains("Want our best stories with fewer ads and alerts when the biggest news stories drop? Download our app")'):
        s.extract()
    for s in soup.select('[itemprop="articleBody"] > p:contains("Get the biggest stories from across")'):
        s.extract()
    article =  soup.select('[itemprop="articleBody"]')[0]
    
async def scan():
    return False
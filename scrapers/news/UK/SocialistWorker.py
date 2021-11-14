Q ='[[wikidata:Q4049684]]'
urls = [
    "https://socialistworker.co.uk/"
]
feeds = [
    "https://socialistworker.co.uk/feed"
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
    headline =  soup.select('[itemprop="headline"]')[0]
    time =  soup.select(".article_view_published")[0]
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('[itemprop="articleBody"] > :not(p)'):
        s.extract()
    # for s in soup.select('.PageContent > .PageStory > :not(p)'):
    #     s.extract()
    # for s in soup.select('div[class="article__detail-text mdc-typography--body1" > script'):
    #     s.extract()
    bodyCopy =  soup.select('[itemprop="articleBody"]')[0]
    
article("https://socialistworker.co.uk/art/52643/Radical+climate+action+is+more+than+slogans")
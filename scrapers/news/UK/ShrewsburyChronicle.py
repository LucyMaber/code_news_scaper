urls = [
    "https://www.shropshirestar.com/"
]
feeds = [
    "https://www.shropshirestar.com/feed"
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
    headline =  soup.select(".story-headline")[0]
    tags =  soup.select(".story-tag-list")[0]
    subheadline =  soup.select(".story-subheadline")[0]
    for s in soup.select('script'):
        s.extract()
    # for s in soup.select('.PageContent > .PageStory > :not(p)'):
    #     s.extract()
    # for s in soup.select('div[class="article__detail-text mdc-typography--body1" > script'):
    #     s.extract()
    bodyCopy =  soup.select('.story-content > div')[0]
    print(bodyCopy)
article("https://www.shropshirestar.com/news/health/2021/11/09/hospital-trust-hoping-for-rapid-move-to-future-fit-next-stage/")
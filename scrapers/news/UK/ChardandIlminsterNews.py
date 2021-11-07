urls = [
    "https://www.chardandilminsternews.co.uk/"
]
feeds = [
    "https://www.carrickfergustimes.co.uk/rss"
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
    hedding =  soup.select('article > .headline ')[0]
    #subhedding =  soup.select('article > h2')[0]
    #tags =  soup.select('.article-tag') [0]
    #time =  soup.select('article > time') [0]
    author_name =  soup.select('author-name > [href=*"/author/profile/"]') [0]
    for s in soup.select('#content-wrapper > div:not(.markup)'):
        s.extract()
    for s in soup.select('#content-wrapper > aside'):
        s.extract()
    # for s in soup.select('#content-wrapper > #axate-wallet'):
    #     s.extract()
    articleBody  =  soup.select('#content-wrapper') [0]
    #print(articleBody)
    print(articleBody)

article("https://www.chardandilminsternews.co.uk/news/19686802.12-15-year-olds-can-use-walk-in-sites-covid-19-vaccinations/")
urls = [
    "https://www.irishtimes.com/"
]
feeds = [
    "https://www.irishtimes.com/rss/test-rss-feed-1.4094403",
    "https://www.irishtimes.com/rss/irish-times-top-10-stories-1.4019566"
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
    headline =  soup.select('.header > hgroup > h1')[0]
    subheadline =  soup.select('.header > hgroup > h2')[0]
    for s in soup.select('.article_bodycopy > :not(p, h1,h2,h3,h4,h5,h6,.twitter-tweet) '):
        s.extract()
    article =  soup.select('.article_bodycopy')[0]
    print(article)
article("https://www.irishtimes.com/news/politics/northern-ireland-s-access-to-single-market-may-be-jeopardised-says-taoiseach-1.4724621")

urls = [
    "http://exiledonline.com/"
]
feeds = [
    "http://exiledonline.com/feed/atom/",
    "http://exiledonline.com/feed/"
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
    headline =  soup.select('#main > .entry > #topslug > a')[0]
    #datePublished =  soup.select('time')[0]
    for s in soup.select('.entry > :not(p,b,h1,h2,h3,h4,h5,h6,strong)'):
        s.extract()
    for s in soup.select('.entry >:not(p,h1,h2,h3,h4,h5,h6)'):
        s.extract()
    for s in soup.select('.entry > p > img'):
        s.extract()
    for s in soup.select('em'):
        s.extract()
    article =  soup.select('.entry')[0]
    print(article)
article("http://exiledonline.com/the-war-nerd-was-there-a-plan-in-afghanistan/")
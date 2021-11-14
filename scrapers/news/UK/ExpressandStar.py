urls = [
    "https://www.expressandstar.com/"
]
feeds = [
    "https://www.expressandstar.com/feed"
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
    headline =      soup.select('.story-headline')[0]
    description =   soup.select('.story-subheadline')[0]
    tags =   soup.select('.story-tag-list')[0]
    #dateModified =  soup.select('time')[0]
    for s in soup.select('figure'):
        s.extract()
    for s in soup.select('script'):
        s.extract()
    articleBody =  soup.select('.story-content > .row')[0]
    
article("https://www.expressandstar.com/news/Features/2021/11/06/photo-exhibition-takes-people-back-to-their-black-country-youth/")
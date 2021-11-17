Q =''
urls = [
    "https://news.sky.com/"
]
feeds = [
    "http://feeds.skynews.com/feeds/rss/home.xml",
    "http://feeds.skynews.com/feeds/rss/world.xml",
    "http://feeds.skynews.com/feeds/rss/uk.xml",
    "http://feeds.skynews.com/feeds/rss/business.xml",
    "http://feeds.skynews.com/feeds/rss/politics.xml",
    "http://feeds.skynews.com/feeds/rss/technology.xml",
    "http://feeds.skynews.com/feeds/rss/entertainment.xml",
    "http://feeds.skynews.com/feeds/rss/entertainment.xml",
    "http://feeds.skynews.com/feeds/rss/strange.xml"
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
    headline =  soup.select('.sdc-site-component-header--h1')[0]
    subheadline =  soup.select('.sdc-article-header__sub-title')[0]
    tags = soup.select('.sdc-article-tags__list')[0]
    for s in soup.select('[data-component-name="sdc-article-body"] > :not(p)'):
        s.extract()
    for s in soup.select('[data-component-name="sdc-article-body"] > :contains("READ THE FULL STORY")'):
        s.extract()
    bodyCopy =  soup.select('[data-component-name="sdc-article-body"]')[0] ### READ THE FULL STORY
    
async def scan():
    return False
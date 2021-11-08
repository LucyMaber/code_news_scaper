urls = [
    "https://www.newspostleader.co.uk/"
]
feeds = [
    "https://www.newspostleader.co.uk/rss"
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
    headline =  soup.select('article > h1')[0]
    subheadline =  soup.select('article > h2')[0]
    for s in soup.select('#content-wrapper > :not(.markup)'):
        s.extract()
    for s in soup.select('#content-wrapper > :contains("READ THE FULL STORY")'):
        s.extract()
    bodyCopy =  soup.select('#content-wrapper')[0] ### READ THE FULL STORY
    print(bodyCopy)
article("https://www.newspostleader.co.uk/news/people/police-targeting-those-spiking-drinks-following-rise-in-cases-in-the-region-3449909")

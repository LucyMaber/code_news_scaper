urls = [
    "https://plantbasednews.org/"
]
feeds = [
    "https://plantbasednews.org/feed/",
    "https://plantbasednews.org/lifestyle/food/start-up-those-vegan-cowboys-cheese/feed/",
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
    headline =  soup.select('h1.entry-title')[0]
    published_time =  soup.select('time.published')[0]
    updated_time =  soup.select('time.updated')[0]
    headline =  soup.select('h1.entry-title')[0]
    subheadline =  soup.select('.newspack-post-subtitle')[0]
    for s in soup.select('img'):
        s.extract()
    for s in soup.select('div.entry-content > :not(p,h1,h2,h3,h4,h5,h6)'):
        s.extract()
    for s in soup.select('script'):
        s.extract()
    bodyCopy =  soup.select('div.entry-content')[0] ### READ THE FULL STORY
    print(bodyCopy)
article("https://plantbasednews.org/lifestyle/food/start-up-those-vegan-cowboys-cheese/")
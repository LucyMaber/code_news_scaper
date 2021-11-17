Q ='[[wikidata:Q293213]]'
urls = [
    "https://www.theguardian.com"
]
feeds = [
    "https://www.theguardian.com/rss",
    "https://www.theguardian.com/uk/rss",
    "https://www.theguardian.com/uk-news/rss",
    "https://www.theguardian.com/world/rss",
    "https://www.theguardian.com/world/coronavirus-outbreak/rss",
    "https://www.theguardian.com/environment/climate-crisis/rss",
    "https://www.theguardian.com/football/rss",
    "https://www.theguardian.com/uk/business/rss",
    "https://www.theguardian.com/uk/environment/rss",
    "https://www.theguardian.com/politics/rss",
    "https://www.theguardian.com/education/rss",
    "https://www.theguardian.com/society/rss",
    "https://www.theguardian.com/science/rss",
    "https://www.theguardian.com/uk/technology/rss",
    "https://www.theguardian.com/global-development/rss",
    "https://www.theguardian.com/tone/obituaries/rss",
    "https://www.theguardian.com/profile/editorial/rss",
    "https://www.theguardian.com/index/contributors/rss",
    "https://www.theguardian.com/cartoons/archive/rss",
    "https://www.theguardian.com/type/video+tone/comment/rss",
    "https://www.theguardian.com/tone/letters/rss",
    "https://www.theguardian.com/uk/film/rss",
    "https://www.theguardian.com/music/rss",
    "https://www.theguardian.com/uk/tv-and-radio/rss",
    "https://www.theguardian.com/books/rss",
    "https://www.theguardian.com/artanddesign/rss",
    "https://www.theguardian.com/stage/rss",
    "https://www.theguardian.com/games/rss",
    "https://www.theguardian.com/music/classical-music-and-opera/rss",
    "https://www.theguardian.com/fashion/rss",
    "https://www.theguardian.com/food/rss",
    "https://www.theguardian.com/tone/recipes/rss",
    "https://www.theguardian.com/lifeandstyle/health-and-wellbeing/rss",
    "https://www.theguardian.com/uk/travel/rss",
    "https://www.theguardian.com/lifeandstyle/women/rss",
    "https://www.theguardian.com/lifeandstyle/men/rss",
    "https://www.theguardian.com/lifeandstyle/love-and-sex/rss",
    "https://www.theguardian.com/fashion/beauty/rss",
    "https://www.theguardian.com/lifeandstyle/home-and-garden/rss",
    "https://www.theguardian.com/uk/money/rss",
    "https://www.theguardian.com/tone/recipes/rss",
    "https://www.theguardian.com/uk/commentisfree/rss",
    "https://www.theguardian.com/uk/culture/rss",
    "https://www.theguardian.com/uk/lifeandstyle/rss"
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
    headline =  soup.select('article > div > div > div > div > div > h1')[0]
    # tags =  soup.select('.tags')[0]
    # datePublished =  soup.select('.datePublished > time')[0]
    # datePublished =  soup.select('.dateModified > time')[0]
    # tags =  soup.select('.tags')[0]
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('#maincontent > div > :not(ul ,p, strong)'):
        s.extract()
    for s in soup.select('[itemprop="articleBody"] > :not(p)'):
        s.extract()
    content =  soup.select('#maincontent > div')[0]
    
async def scan():
    return False
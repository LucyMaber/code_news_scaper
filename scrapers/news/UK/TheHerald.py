urls = [
    "https://www.heraldscotland.com/"
]
feeds = [
    "https://www.heraldscotland.com/news/rss/",
    "https://www.heraldscotland.com/news/coronavirus/rss/",
    "https://www.heraldscotland.com/news/health/rss/",
    "https://www.heraldscotland.com/news/education/rss/",
    "https://www.heraldscotland.com/news/transport/rss/",
    "https://www.heraldscotland.com/news/world_news/rss/",
    "https://www.heraldscotland.com/news/environment/rss/",
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
    headline =  soup.select('h1.headline')[0]
    # tags =  soup.select('.tags')[0]
    # datePublished =  soup.select('.datePublished > time')[0]
    # datePublished =  soup.select('.dateModified > time')[0]
    # tags =  soup.select('.tags')[0]
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('#maincontent > div > :not(ul ,p, strong)'):
        s.extract()
    for s in soup.select('#subscription-content > :not(p)'):
        s.extract()
    content =  soup.select('.article-body')[0]
    print(content)
article("https://www.heraldscotland.com/politics/19707778.net-zero-planning-shake-up-town-retail-penalised-regeneration-favoured/")

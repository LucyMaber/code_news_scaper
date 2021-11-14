urls =[
    "https://www.express.co.uk/"
]
feeds = [
    "https://www.express.co.uk/posts/rss/77/news",
    "https://www.express.co.uk/posts/rss/1/uk",
    "https://www.express.co.uk/posts/rss/106/royal",
    "https://www.express.co.uk/posts/rss/139/politics",
    "https://www.express.co.uk/posts/rss/128/nature",
    "https://www.express.co.uk/posts/rss/80/weird",
    "https://www.express.co.uk/posts/rss/151/science",
    "https://www.express.co.uk/posts/rss/54/sunday",
    "https://www.express.co.uk/posts/rss/141/history",
    "https://www.express.co.uk/posts/rss/140/obituaries",
    "https://www.express.co.uk/posts/rss/149/clarificationsandcorrections",
    "https://www.express.co.uk/posts/rss/79/celebritynews",
    "https://www.express.co.uk/posts/rss/18/entertainment",
    "https://www.express.co.uk/posts/rss/36/films",
    "https://www.express.co.uk/posts/rss/130/life",
    "https://www.express.co.uk/posts/rss/13/garden",
    "https://www.express.co.uk/posts/rss/11/health",
    "https://www.express.co.uk/posts/rss/59/tech",

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
    headline =  soup.select('header > h1')[0]
    description =  soup.select('header > h3')[0]
    author =  soup.select('.author > a')[0]
    time =  soup.select('.dates > time')[0]
    for s in soup.select('article > div > div > div:not(.text-description)'):
        s.extract()
    for s in soup.select('article > div > div > div:contains("READ MORE:")'):
        s.extract()
    for s in soup.select('article > div > div > div:contains("DON\'T MISS:")'):
        s.extract()
    articleBody =  soup.select('article > div > div')[0]
    
article("https://www.express.co.uk/news/politics/1516560/eu-news-eu-fisheries-funds-Netherlands-dutch-fishermen-france")
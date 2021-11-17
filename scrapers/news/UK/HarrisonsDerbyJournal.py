Q =""
urls = [
    "https://www.hastingsobserver.co.uk/"
]
feeds = [
"https://www.hastingsobserver.co.uk/news/traffic-and-travel/rss",
"https://www.hastingsobserver.co.uk/news/crime",
"https://www.hastingsobserver.co.uk/news/weather",
"https://www.hastingsobserver.co.uk/news/politics",
"https://www.hastingsobserver.co.uk/business",
"https://www.hastingsobserver.co.uk/education",
"https://www.hastingsobserver.co.uk/health",
"https://www.hastingsobserver.co.uk/news/opinion",
"https://www.hastingsobserver.co.uk/news/people",
"https://www.hastingsobserver.co.uk/read-this",
"https://www.hastingsobserver.co.uk/retro",
"https://www.hastingsobserver.co.uk/recommended/entertainment",
"https://www.hastingsobserver.co.uk/recommended/technology",
"https://www.hastingsobserver.co.uk/recommended/lifestyle",
"https://www.hastingsobserver.co.uk/recommended/home-and-garden",
"https://www.hastingsobserver.co.uk/recommended/fashion-and-beauty",
"https://www.hastingsobserver.co.uk/recommended/deals",
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
    headline =  soup.select('.article__title')[0]
    for s in soup.select('.article__detail-text > :not(p)'):
        s.extract()
    article =  soup.select('.article__detail-text')[0]
    
async def scan():
    return False### NEED JAVASCRIPT
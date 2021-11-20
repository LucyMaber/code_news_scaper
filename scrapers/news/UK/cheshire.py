Q =''
urls = [
    "https://www.cheshire-live.co.uk/"
]
feeds = [
    "https://www.cheshire-live.co.uk/",
    "https://www.cheshire-live.co.uk/news/uk-world-news/",
    "https://www.cheshire-live.co.uk/news/motoring/",
    "https://www.cheshire-live.co.uk/news/history/",
    "https://www.cheshire-live.co.uk/news/showbiz/",
    "https://www.cheshire-live.co.uk/news/health/",
    "https://www.cheshire-live.co.uk/all-about/education/",
    "https://www.cheshire-live.co.uk/all-about/politics/",
    "https://www.cheshire-live.co.uk/all-about/traffic-and-travel/",
    "https://www.cheshire-live.co.uk/all-about/crime/",
    "https://www.cheshire-live.co.uk/all-about/cheshire/",
    "https://www.cheshire-live.co.uk/news/",
    "https://www.cheshire-live.co.uk/",
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
    # Need to add author
    article_body =  soup.select(".p402_hide")[0]
    for s in soup.select("script"):
        s.extract()
    headline =  soup.select('h1.headline')
    
async def scan():
    return False
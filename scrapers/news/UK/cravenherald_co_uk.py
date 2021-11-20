Q ='Q5182740'
urls = [
    "https://www.cravenherald.co.uk/"
]
feeds = [
    "https://www.cravenherald.co.uk/news/rss/",
    "https://www.cravenherald.co.uk/news/localnews/rss/",
    "https://www.cravenherald.co.uk/news/farming/rss/",
    "https://www.cravenherald.co.uk/news/business/rss/",
    "https://www.cravenherald.co.uk/opinion/opinion_letters/rss/",
    "https://www.cravenherald.co.uk/opinion/opinion_leader/rss/",
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
    title =  soup.select('h1.headline ')[0]
    for s in soup.select("script"):
        s.extract()
    articleBody =  soup.select('.p402_hide')[0]
    
async def scan():
    return False
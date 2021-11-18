Q =''
urls = [
    "https://www.theboltonnews.co.uk/"
]
feeds = [
"https://www.theboltonnews.co.uk/news/bolton/rss/",
"https://www.theboltonnews.co.uk/news/farnworth/rss/",
"https://www.theboltonnews.co.uk/news/westhoughton/rss/",
"https://www.theboltonnews.co.uk/news/horwich/rss/",
"https://www.theboltonnews.co.uk/news/crime/rss/",
"https://www.theboltonnews.co.uk/news/business/rss/",
"https://www.theboltonnews.co.uk/news/business/rss/",
"https://www.theboltonnews.co.uk/news/entertainment/rss/",
"https://www.theboltonnews.co.uk/news/coronavirus/rss/",
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
    headline =  soup.select('.headline ')[0]
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('img'):
        s.extract()
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('#subscription-content > figure'):
        s.extract()
    for s in soup.select('#subscription-content > div'):
        s.extract()
    bodyCopy = soup.select('.article-body')[0]
    
async def scan():
    return False
Q ='[[wikidata:Q5416645]]'
urls = [
    "https://www.glasgowtimes.co.uk"
]
feeds = [
"https://www.glasgowtimes.co.uk/news/health/rss/",
"https://www.glasgowtimes.co.uk/news/glasgow-crime/rss",
"https://www.glasgowtimes.co.uk/news/councilandpoliics/rss",
"https://www.glasgowtimes.co.uk/news/planning-development/rss",
"https://www.glasgowtimes.co.uk/news/glasgow-city-centre/rss",
"https://www.glasgowtimes.co.uk/news/glasgow-southside/rss",
"https://www.glasgowtimes.co.uk/news/glasgow-east-end/rss",
"https://www.glasgowtimes.co.uk/news/glasgow-west-end/rss",
"https://www.glasgowtimes.co.uk/news/north-glasgow/rss",
"https://www.glasgowtimes.co.uk/news/best-of/rss",
"https://www.glasgowtimes.co.uk/news/rss",
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
    description =  soup.select('[itemprop="description"]')[0]
    # description =  soup.select('h3.entry-title')[0]
    # author =  soup.select('.author > a')[0]
    # time =  soup.select('.dates > time')[0]
    for s in soup.select('.subscription-content > :not(p)'):
        s.extract()
    for s in soup.select('p > :contains("READ MORE")'):
        s.extract()
    for s in soup.select('p > :contains("Get all the stories you love straight")'):
        s.extract()
    for s in soup.select('p > :contains("We would love to hear about it")'):
        s.extract()
    for s in soup.select('p > :contains("straight to your inbox")'):
        s.extract()
    for s in soup.select('script'):
        s.extract()
    content =  soup.select('.p402_hide')[0]
    
async def scan():
    return False
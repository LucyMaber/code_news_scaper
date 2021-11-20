Q ='[[wikidata:Q7300490]]'
urls = [
    "https://www.readingchronicle.co.uk/"
]
feeds = [
    "https://www.readingchronicle.co.uk/news/rss/",
    "https://www.readingchronicle.co.uk/sport/rss/",
    "https://www.readingchronicle.co.uk/news/readingretailawards2019/rss/",
    "https://www.readingchronicle.co.uk/news/around/rss/",
    "https://www.readingchronicle.co.uk/news/around/caversham/rss/",
    "https://www.readingchronicle.co.uk/news/around/tilehurst/rss/",
    "https://www.readingchronicle.co.uk/news/around/whitley/rss/",
    "https://www.readingchronicle.co.uk/news/around/east_reading/rss/",
    "https://www.readingchronicle.co.uk/news/around/west_reading/rss/",
    "https://www.readingchronicle.co.uk/news/around/southcote/rss/",
    "https://www.readingchronicle.co.uk/news/around/calcot/rss/",
    "https://www.readingchronicle.co.uk/news/around/calcot/rss/",
    "https://www.readingchronicle.co.uk/news/around/coley/rss/",
    "https://www.readingchronicle.co.uk/news/around/katesgrove/rss/",
    "https://www.readingchronicle.co.uk/news/around/villages/rss/",
    "https://www.readingchronicle.co.uk/news/central/rss/",
    "https://www.readingchronicle.co.uk/news/woodleyandearley/rss/",
    "https://www.readingchronicle.co.uk/news/woodleyandearley/earley/rss/",
    "https://www.readingchronicle.co.uk/news/woodleyandearley/lower_earley/rss/",
    "https://www.readingchronicle.co.uk/news/woodleyandearley/woodley/rss/",
    "https://www.readingchronicle.co.uk/news/west_berkshire/rss/"
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
    for s in soup.select('img'):
        s.extract()
    for s in soup.select('.p402_hide > :not(p,h2,h3,h4,h5,h6)'):
        s.extract()
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('.p402_hide > p:contains("READ MORE")'):
        s.extract()
    bodyCopy =  soup.select('.article-body')[0] ### READ THE FULL STORY
    
async def scan():
    return False
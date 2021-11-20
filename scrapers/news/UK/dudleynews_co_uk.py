Q ='[[wikidata:Q5311863]]'
urls = [
    "https://www.dudleynews.co.uk/"
]
feeds = [
    "https://www.dudleynews.co.uk/news/rss/",
    "https://www.dudleynews.co.uk/news/local/rss/",
    "https://www.dudleynews.co.uk/news/local/your_community/ab/rss/",
    "https://www.dudleynews.co.uk/news/local/your_community/cd/rss/",
    "https://www.dudleynews.co.uk/news/local/your_community/cd/dudley/rss/",
    "https://www.dudleynews.co.uk/news/local/your_community/gh/rss/",
    "https://www.dudleynews.co.uk/news/local/your_community/kl/rss/",
    "https://www.dudleynews.co.uk/news/local/your_community/kl/kingswinford/rss/",
    "https://www.dudleynews.co.uk/news/local/your_community/op/rss/",
    "https://www.dudleynews.co.uk/news/local/your_community/op/pensnett/rss/",
    "hhttps://www.dudleynews.co.uk/news/local/your_community/st/rss/",
    "https://www.dudleynews.co.uk/news/local/your_community/op/pensnett/rss/",
    "https://www.dudleynews.co.uk/news/local/your_community/st/rss/",
    "https://www.dudleynews.co.uk/news/local/your_community/st/sedgley/rss/",
    "https://www.dudleynews.co.uk/news/business_daily/rss/",
    "https://www.dudleynews.co.uk/news/business_daily/bizblogs/rss/",
    "https://www.dudleynews.co.uk/news/general-election/rss/",
    "https://www.dudleynews.co.uk/news/coronavirus/rss/",
    "https://www.dudleynews.co.uk/news/national/rss/",
    "https://www.dudleynews.co.uk/news/national/uk-today/rss/",
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
    for s in soup.select('div.cell_right_sub1 > a > img'):
        s.extract()
    bodyCopy =  soup.select('div.p402_hide')[0]
    
async def scan():
    return False
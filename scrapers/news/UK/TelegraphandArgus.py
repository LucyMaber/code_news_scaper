Q =''
urls = [
    "https://www.thetelegraphandargus.co.uk/"
]
feeds = [
"https://www.thetelegraphandargus.co.uk/news/rss/",
"https://www.thetelegraphandargus.co.uk/news/localbrad/rss/",
"https://www.thetelegraphandargus.co.uk/news/keighleynews/rss/",
"https://www.thetelegraphandargus.co.uk/news/airelocal/rss/",
"https://www.thetelegraphandargus.co.uk/news/ilkleynews/rss/",
"https://www.thetelegraphandargus.co.uk/news/uk_today_homepage/rss/",
"https://www.thetelegraphandargus.co.uk/news/bradford-means-business-awards/rss/",
"https://www.thetelegraphandargus.co.uk/news/coronavirus/rss/",
"https://www.thetelegraphandargus.co.uk/opinion/rss/",
"https://www.thetelegraphandargus.co.uk/opinion/columnists/rss/",
"https://www.thetelegraphandargus.co.uk/opinion/columnists/columnistshelenmead/rss/",
"https://www.thetelegraphandargus.co.uk/opinion/columnists/opinion_emma/rss/",
"https://www.thetelegraphandargus.co.uk/opinion/columnists/news_opinion_columnist_keith/rss/",
"https://www.thetelegraphandargus.co.uk/opinion/columnists/timmurgatroyd/rss/",
"https://www.thetelegraphandargus.co.uk/opinion/columnists/chrismoncrieff/rss/",
"https://www.thetelegraphandargus.co.uk/opinion/comment/rss/",
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
    headline =  soup.select('#article > .headline ')[0]
    datePublished =  soup.select('[itemprop="datePublished"]')[0]
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('.adMediumRectangle'):
        s.extract()
    for s in soup.select('#subscription-content >:not(p,h1,h2,h3,h4,h5,h6,strong)'):
        s.extract()
    try:
        bodyCopy = soup.select('.livefeed-summary')[0]
    except:
        bodyCopy = soup.select('.p402_hide')[0]
    
async def scan():
    return False
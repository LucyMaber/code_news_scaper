Q ='[[wikidata:Q15043341]]'
urls = [
    "https://www.oxfordmail.co.uk/"
]
feeds = [
    "https://www.oxfordmail.co.uk/news/rss/",
    "https://www.oxfordmail.co.uk/news/yourtown/oxfordshire/rss/",
    "https://www.oxfordmail.co.uk/news/yourtown/oxford/rss/",
    "https://www.oxfordmail.co.uk/news/yourtown/abingdon/rss/",
    "https://www.oxfordmail.co.uk/news/yourtown/banbury/rss/",
    "https://www.oxfordmail.co.uk/news/yourtown/bicester/rss/",
    "https://www.oxfordmail.co.uk/news/yourtown/didcot/rss/",
    "https://www.oxfordmail.co.uk/news/yourtown/wallingford/rss/",
    "https://www.oxfordmail.co.uk/news/yourtown/wantage/rss/",
    "https://www.oxfordmail.co.uk/news/yourtown/witney/rss/",
    "https://www.oxfordmail.co.uk/news/yourtown/vale/rss/",
    "https://www.oxfordmail.co.uk/news/yourtown/south_oxon/rss/",
    "https://www.oxfordmail.co.uk/news/yourtown/cherwell/rss/",
    "https://www.oxfordmail.co.uk/news/crime/rss/",
    "https://www.oxfordmail.co.uk/news/opinion/columns/rss/",
    "https://www.oxfordmail.co.uk/news/opinion/columns/billheinecolumn/rss/",
    "https://www.oxfordmail.co.uk/news/opinion/columns/on_yer_bike/rss/",
    "https://www.oxfordmail.co.uk/news/opinion/columns/cabbages/rss/",
    "https://www.oxfordmail.co.uk/news/opinion/columns/legal/rss/",
    "https://www.oxfordmail.co.uk/news/opinion/columns/insider/rss/",
    "https://www.oxfordmail.co.uk/news/opinion/columns/faith/rss/",
    "https://www.oxfordmail.co.uk/news/opinion/yourblogs/rss/",
    "https://www.oxfordmail.co.uk/news/opinion/columns/faith/rss/",
    "https://www.oxfordmail.co.uk/news/insta/rss/",
    "https://www.oxfordmail.co.uk/news/news_bites/rss/",
    "https://www.oxfordmail.co.uk/news/yourtown/vale/rss/",
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
    headline =  soup.select('h1.headline ')[0]
    time =  soup.select('[itemprop="datePublished"]')[0]
    for s in soup.select('.article-first-paragraph > :not(p,h2)'):
        s.extract()
    for s in soup.select('img'):
        s.extract()
    for s in soup.select('script'):
        s.extract()
    bodyCopy =  soup.select('.p402_hide')[0] ### READ THE FULL STORY
    
async def scan():
    return False

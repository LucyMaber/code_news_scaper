Q ='[[wikidata:Q7757848]]'
urls = [
    "https://www.bristolpost.co.uk/"
]
feeds = [
"https://www.bristolpost.co.uk/news/rss.xml",
"https://www.bristolpost.co.uk/news/bristol-news/rss.xml",
"https://www.bristolpost.co.uk/all-about/education/rss.xml",
"https://www.bristolpost.co.uk/news/health/rss.xml",
"https://www.bristolpost.co.uk/all-about/politics/rss.xml",
"https://www.bristolpost.co.uk/all-about/traffic-travel/rss.xml",
"https://www.bristolpost.co.uk/news/history/rss.xml",
"https://www.bristolpost.co.uk/news/celebs-tv/rss.xml",
"https://www.bristolpost.co.uk/news/property/rss.xml",
"https://www.bristolpost.co.uk/news/motoring/rss.xml",
"https://www.bristolpost.co.uk/news/jobs/rss.xml",
"https://www.bristolpost.co.uk/news/uk-world-news/rss.xml"
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
    hedding =  soup.select('div.headline-with-subtype') [0]
    subhedding =  soup.select('[itemprop="description"]') [0]
    publishedTime =  soup.select('.date-published') [0]
    by =  soup.select('.author > a.publication-theme') [0]
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('p:has(b)'):
        s.extract()
    for s in soup.select('figure'):
        s.extract()
    for s in soup.select('reach-mpu'):
        s.extract()
    for s in soup.select('reach-adyoulike'):
        s.extract()
    for s in soup.select('section'):
        s.extract()
    for s in soup.select('reach-taboola'):
        s.extract()
    for s in soup.select('reach-converse'):
        s.extract()
    for s in soup.select('reach-adyoulike'):
        s.extract()
    for s in soup.select('.html-embed'):
        s.extract()
    for s in soup.select('p:has(b)'):
        s.extract()
    acale =  soup.select('[itemprop="articleBody"]') [0]
    
async def scan():
    return False

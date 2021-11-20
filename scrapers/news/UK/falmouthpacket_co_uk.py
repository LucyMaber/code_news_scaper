Q ='[[wikidata:Q7122996]]'
urls = [
    "https://www.falmouthpacket.co.uk/"
]
feeds = [
"https://www.falmouthpacket.co.uk/news/rss/",
"https://www.falmouthpacket.co.uk/news/fpfalmouth/rss/",
"https://www.falmouthpacket.co.uk/news/helstonandporthleven/rss/",
"https://www.falmouthpacket.co.uk/news/camborneandredruth/rss/",
"https://www.falmouthpacket.co.uk/news/truro/rss/",
"https://www.falmouthpacket.co.uk/news/westcornwall/rss/",
"https://www.falmouthpacket.co.uk/news/business/rss/",
"https://www.falmouthpacket.co.uk/news/truro_college/rss/",
"https://www.falmouthpacket.co.uk/news/general-election/rss/",
"https://www.falmouthpacket.co.uk/news/coronavirus/rss/",
"https://www.falmouthpacket.co.uk/lettersandcomment/readerswrite/rss/",
"https://www.falmouthpacket.co.uk/lettersandcomment/skipper/rss/",


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

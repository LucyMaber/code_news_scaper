Q ='Q67311447'
urls = [
    "https://www.football.london/"
]
feeds = [
    "https://www.football.london/rss.xml",
    "https://www.football.london/arsenal-fc/?service=rss",
    "https://www.football.london/chelsea-fc/?service=rss",
    "https://www.football.london/chelsea-fc/?service=rss",
    "https://www.football.london/tottenham-hotspur-fc/?service=rss",
    "https://www.football.london/west-ham-united-fc/?service=rss",
    "https://www.football.london/crystal-palace-fc/?service=rss",
    "https://www.football.london/watford-fc/?service=rss",
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
    headline =  soup.select('article > h1')[0]
    description =  soup.select('.sub-title')[0]
    # description =  soup.select('h3.entry-title')[0]
    # author =  soup.select('.author > a')[0]
    # time =  soup.select('.dates > time')[0]
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('.live-event-lead-entry > :not(p)'):
        s.extract()
    artcal =  soup.select('.live-event-lead-entry')[0]
    

async def scan():
    return False
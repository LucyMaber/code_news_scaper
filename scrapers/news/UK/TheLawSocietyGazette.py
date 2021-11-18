Q ='[[wikidata:Q7746393]]'
urls = [
    "https://www.lawgazette.co.uk/"
]
feeds = [
    "https://www.lawgazette.co.uk/17.rss"
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
    req = requests.get(url,headers=header)
    content = req.content
    soup = BeautifulSoup(content, 'html.parser')
    story_title =  soup.select('.story_title > h1')[0]
    content =  soup.select('.articleContent')[0]
    
async def scan():
    return False
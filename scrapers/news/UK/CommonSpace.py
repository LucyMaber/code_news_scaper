urls = [
    "https://sourcenews.scot/"
]
feeds = [
 "https://sourcenews.scot/feed/"
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
    # Need to add author
    article_subtitle =  soup.select(".container > div > div >  p")[0]
    article_title =  soup.select(".entry-title")[0]
    time =  soup.select(".entry-date")[0]
    for s in soup.select("script"):
        s.extract()
    entry_content =  soup.select(".entry-content")[0]
    
article("https://sourcenews.scot/source-direct-independence-fantasy-and-reality/")

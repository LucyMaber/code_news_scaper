urls = [
    "https://www.glasgowworld.com/"
]
feeds = [
    "https://www.glasgowworld.com/rss"
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
    headline =  soup.select("#content-wrapper > h1 ")[0]
    subheadline =  soup.select("#content-wrapper > h2 ")[0]
    #time =  soup.select("article > time")[0]
    #author =  soup.select(".author-name > a")[0]
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('div.article-content > :not(.markup)'):
        s.extract()
    bodyCopy =  soup.select("div.article-content")[0]
    
article("https://www.glasgowworld.com/news/cop26-thousands-of-protesters-in-glasgow-for-global-day-of-action-3447945")
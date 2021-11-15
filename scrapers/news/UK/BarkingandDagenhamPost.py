Q =''
urls = [
    "https://www.barkinganddagenhampost.co.uk/"
]
feeds = [

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
    #headline =  soup.select('h1.article__title') [0]
    for s in soup.select(".item-videos-jw"):
        s.extract()
    for s in soup.select(".most-read"):
        s.extract()
    for s in soup.select("img"):
        s.extract()
    for s in soup.select("div.article__detail-text > div"):
        s.extract()
    article_body =  soup.select('div.article__detail-text') [0]
    
article("https://www.barkinganddagenhampost.co.uk/news/traffic/road-and-rail-delays-to-avoid-november-1-8449954")
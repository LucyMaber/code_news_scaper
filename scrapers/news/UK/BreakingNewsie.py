Q =''
urls = [
    "https://www.breakingnews.ie/"
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
    hedding =  soup.select(' div > div > h1') [0]
    time =  soup.select('div > time') [0]
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('article > div:not(.twitter-tweet)'):
        s.extract()
    article_body =  soup.select('article') [0]
    
article("https://www.breakingnews.ie/entertainment/jessica-simpson-celebrates-four-years-of-being-sober-1207860.html")
urls = [
    "https://www.irishpost.com/"
]
feeds = [
    "https://www.irishpost.com/feed"
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
    headline =  soup.select('.caption-text > h1')[0]
    for s in soup.select('#article-body > :not(p, h1,h2,h3,h4,h5,h6,.twitter-tweet) '):
        s.extract()
    article =  soup.select('#article-body')[0]
    
article("https://www.irishpost.com/sport/seizure-of-banned-animal-remedies-occurs-during-raid-on-irish-horse-racing-yard-223840")

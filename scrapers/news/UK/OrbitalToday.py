urls = [
    "https://orbitaltoday.com/"
]
feeds = [
    "https://orbitaltoday.com/feed"
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
    headline =  soup.select('h1.chapter-ttl')[0]
    for s in soup.select('.article-chapter > :not(p,h2)'):
        s.extract()
    for s in soup.select('img'):
        s.extract()
    for s in soup.select('script'):
        s.extract()
    bodyCopy =  soup.select('.article-chapter')[0] ### READ THE FULL STORY
    print(bodyCopy)
article("https://orbitaltoday.com/2021/11/08/peter-beck-from-rocket-lab-shares-the-reason-behind-his-motivation/")


Q =''
urls = [
    "https://theedinburghreporter.co.uk/"
]
feeds = [
    "https://theedinburghreporter.co.uk/feed/"
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
    headline =  soup.select('h1.entry-title')[0]
    time =  soup.select('.entry-date')[0]
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('img'):
        s.extract()
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('iframe'):
        s.extract()
    for s in soup.select('.td-post-content > :not(p,h1,h2,h3,h4,h5,.wp-block-embed-twitter)'):
        s.extract()
    bodyCopy = soup.select('.td-post-content')[0]
    
article("https://theedinburghreporter.co.uk/2021/11/all-three-christmas-planning-applications-recommended-for-approval/")
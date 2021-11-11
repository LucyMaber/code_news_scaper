urls = [
    "https://www.law.com/"
]
feeds = [

]
header={
    # 'sec-ch-ua': 'Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': 'Linux',
    # 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
}


from bs4 import BeautifulSoup
import requests

def article(url):
    req = requests.get(url,headers=header)
    content = req.content
    soup = BeautifulSoup(content, 'html.parser')
    headline =  soup.select('h1.article-headline')[0]
    subheadline =  soup.select('p.hdr-description')[0]
    tiem =  soup.select('.pubdate')[0]
    tags =  soup.select('.primary-cat')[0]
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('.access-body > :not(p)'):
        s.extract()
    content =  soup.select('.access-body')[0]
    print(tags)
article("https://www.law.com/international-edition/2021/11/10/us-investigates-tencents-1-3b-acquisition-of-british-videogame-maker/")

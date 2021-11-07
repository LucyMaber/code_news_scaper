urls = [
    "https://www.motorcyclenews.com/"
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
    headline =  soup.select('#article > div > div > h1')[0]
    #time =  soup.select("article > time")[0]
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('style'):
        s.extract()
    for s in soup.select('.p402_premium >:not(p,h1,h2,h3,h4,h5,h6,strong)'):
        s.extract()
    articleBody =  soup.select('.p402_premium')[0]
    print(articleBody)
article("https://www.motorcyclenews.com/news/new-tech/aegis-rider-ag/")

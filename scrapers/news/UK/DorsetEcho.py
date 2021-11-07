urls = [
    "https://www.dorsetecho.co.uk/"
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
    headline =  soup.select('#article > .headline')[0]
    author =  soup.select('.author-name')[0]
    #subheadline =  soup.select('article > h2 ')[0]
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('#subscription-content > div'):
        s.extract()
    for s in soup.select('#subscription-content > div'):
        s.extract()
    for s in soup.select('#subscription-content > ul'):
        s.extract()
    for s in soup.select('#subscription-content > img'):
        s.extract()
    bodyCopy =  soup.select('.p402_hide')[0]
    print(bodyCopy)
article("https://www.dorsetecho.co.uk/news/19692080.tributes-paid-selfless-passionate-youtuber-died-crash-dorset-route/")
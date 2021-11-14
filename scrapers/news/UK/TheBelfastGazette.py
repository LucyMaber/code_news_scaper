urls = [
    "https://www.thegazette.co.uk/"
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
    headline =  soup.select('header > .title')[0]
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('img'):
        s.extract()
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('article > p:first-child'):
        s.extract()
    for s in soup.select('article > div > p:has(em)'):
        s.extract()
    for s in soup.select('article > div >  :contains("See also") ~ *'):
        s.extract()
    bodyCopy = soup.select('article > div')[0]
    
article("https://www.thegazette.co.uk/all-notices/content/103996/")
## ERROR uninow
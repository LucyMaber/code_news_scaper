urls = [
    "https://www.greenocktelegraph.co.uk/"
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
    headline =  soup.select('h1.headline ')[0]
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('.subscription-content > :not(ul ,p, strong)'):
        s.extract()
    for s in soup.select('a[data-link-tracking="InArticle|Link"]'):
        s.extract()
    for s in soup.select('p > :-soup-contains("READ MORE:")'):
        s.extract()
    for s in soup.select('p > :-soup-contains("Get the biggest stories")'):
        s.extract()
    for s in soup.select('p > :-soup-contains("please log in and leave you comments below.")'):
        s.extract()
    content =  soup.select('.p402_hide')[0]
    
article("https://www.greenocktelegraph.co.uk/news/19694121.7m-investment-project-loch-thom-wins-scottish-civil-engineering-award/")
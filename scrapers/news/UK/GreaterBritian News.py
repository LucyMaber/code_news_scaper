urls = [
    "https://www.gbnews.uk/"
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
    headline =  soup.select('[itemprop="headline"]')[0]
    tags =  soup.select('.tags')[0]
    datePublished =  soup.select('.datePublished > time')[0]
    datePublished =  soup.select('.dateModified > time')[0]
    tags =  soup.select('.tags')[0]
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('.bodytext > :not(ul ,p, strong)'):
        s.extract()
    content =  soup.select('.bodytext')[0]
    
article("https://www.gbnews.uk/news/covid-booster-jab-bookings-extended-to-a-month-in-advance/154362")
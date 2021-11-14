urls = [
    "https://moneyweek.com/"
]
feeds = [
    "https://subscription.moneyweek.co.uk/rss.xml"
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
    headline =  soup.select('h1.polaris__heading')[0]
    subheadline =  soup.select('#main > div > h2')[0]
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('[class="polaris__content polaris__simple-grid -body-copy"] > :not(.polaris__simple-grid--main)'):
        s.extract()
    for s in soup.select('[class="polaris__simple-grid--main"] > .polaris__primary-media'):
        s.extract()
    for s in soup.select('.polaris__content-bottom'):
        s.extract()
    for s in soup.select('.polaris__related-links--list-item'):
        s.extract()
    bodyCopy =  soup.select('[class="polaris__content polaris__simple-grid -body-copy"]')[0]
    
article("https://moneyweek.com/economy/global-economy/604074/central-banks-are-still-sticking-to-the-plan-on-inflation/")

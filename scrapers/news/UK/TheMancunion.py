urls = [
    "https://mancunion.com/"
]
feeds = [
    "https://mancunion.com/feed"
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
    headline =  soup.select('.uk-article-title')[0]
    time =  soup.select('time')[0]
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('img'):
        s.extract()
    for s in soup.select(".uk-grid > .uk-width-large-4-6 > :not(p)"):
        s.extract()
    content =  soup.select('.uk-grid > .uk-width-large-4-6')[0]
    print(content)
article("https://mancunion.com/2021/11/06/university-of-manchester-staff-to-strike-over-pay/")

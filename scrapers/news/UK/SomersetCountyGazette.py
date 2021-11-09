urls = [
    "https://www.somersetcountygazette.co.uk/"
]
feeds = [
    "https://www.somersetcountygazette.co.uk/news/rss/"
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
    headline =  soup.select('.headline ')[0]
    # for s in soup.select('.article-wrapper > :not(p,b,h1,h2,h3,h4,h5,h6,strong)'):
    #     s.extract()
    for s in soup.select('#subscription-content > :not(p, h1,h2,h3,h4,h5,h6) '):
        s.extract()
    for s in soup.select('#subscription-content > p:contains("READ MORE")'):
        s.extract()
    article =  soup.select('#subscription-content')[0]
    print(article)
article("https://www.somersetcountygazette.co.uk/news/19704289.next-steps-revealed-single-unitary-authority-somerset/")

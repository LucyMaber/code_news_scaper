urls = [
    "https://bylinetimes.com/"
]
feeds = [
    "https://bylinetimes.com/feed"
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
    hedding =  soup.select('h1.wp-block-fabrica-headline')[0]
    publishedTime =  soup.select('.date') [0]
    by =  soup.select('.byline') [0]
    # tags =  soup.select('.article-tag') [0]
    for s in soup.select('.bodyText > div'):
        s.extract()
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('.has-text-align-center'):
        s.extract()
    for s in soup.select('.wp-block-image'):
        s.extract()
    for s in soup.select('.bodyText > .wp-block-image'):
        s.extract()
    article_body =  soup.select_one('.bodyText')
    print(hedding.getText())
article("https://bylinetimes.com/2021/11/02/hot-air-and-wind-why-johnsons-cop-looks-likely-to-flop/")
#frameInner > article > div.sc-bmyXtO.darZld > div.sc-jtggT.iedqFq > div:nth-child(2)
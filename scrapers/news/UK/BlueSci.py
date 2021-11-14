urls = [
    "https://www.bluesci.co.uk/"
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
    headline =  soup.select_one('.page-title > div')
    description =  soup.select_one('.page-desc > div')
    published =  soup.select_one(".featured-date")
    article_body =  soup.select('.page-content > div >span') [0]
    #for s in soup.select('#content-wrapper >div:not(.markup)'):
    #    s.extract()
    for s in soup.select('.ad-placeholder'):
        s.extract()
    
article("https://www.bluesci.co.uk/posts/changing-climate-alters-how-volcanic-eruptions-affect-our-planet")
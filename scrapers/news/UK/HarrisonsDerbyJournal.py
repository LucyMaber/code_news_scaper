Q =""
urls = [
    "https://www.hastingsobserver.co.uk/"
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
    headline =  soup.select('.article__title')[0]
    for s in soup.select('.article__detail-text > :not(p)'):
        s.extract()
    article =  soup.select('.article__detail-text')[0]
    
article("https://www.hamhigh.co.uk/news/products-recalled-due-to-safety-concerns-november-5-8465994")
### NEED JAVASCRIPT
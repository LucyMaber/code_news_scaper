Q =""
urls = [
    "https://www.test-and-measurement-world.com/"
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
    content = requests.get(url,headers=header, verify=False).content
    soup = BeautifulSoup(content, 'html.parser')
    headline =  soup.select('article > h2 ')[0]
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('article > :not(p,h1,h2,h3,h4,h5,h6,strong)'):
        s.extract()
    bodyCopy = soup.select('article')[0]
    
article("https://www.test-and-measurement-world.com/Articles/Mobile-phone-hardware-testing-and-repairing.html")
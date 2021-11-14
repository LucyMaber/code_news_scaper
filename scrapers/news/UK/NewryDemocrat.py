urls = [
    "https://www.newrydemocrat.com/"
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
    headline =  soup.select('[itemprop="headline name"]')[0]
    author =  soup.select('.author_name_value')[0]
    time =  soup.select('[itemprop="datePublished"]')[0]
    for s in soup.select('[itemprop="text"] > div > :not(p)'):
        s.extract()
    bodyCopy =  soup.select('[itemprop="text"] > div')[0]
    
article("https://www.newrydemocrat.com/sport/2021/10/24/gallery/toothless-city-drop-three-vital-points-19331/")

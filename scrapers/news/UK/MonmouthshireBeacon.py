urls = [
    "https://www.monmouthshirebeacon.co.uk/"
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
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('[itemscope="itemscope"] > :not(p)'):
        s.extract()
    bodyCopy =  soup.select('[itemscope="itemscope"]')[0]
    print(bodyCopy)
article("https://www.monmouthshirebeacon.co.uk/article.cfm?id=118608&headline=Two%20rare%20vintage%20tractors%20up%20for%20sale%20in%20antiques%20auction&sectionIs=news&searchyear=2021")

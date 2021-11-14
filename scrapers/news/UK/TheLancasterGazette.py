urls = [
    "https://eu.lancastereaglegazette.com/"
]
feeds = [

]
header={
    # 'sec-ch-ua': 'Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': 'Linux',
    # 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
}


from bs4 import BeautifulSoup
import requests

def article(url):
    req = requests.get(url,headers=header)
    content = req.content
    soup = BeautifulSoup(content, 'html.parser')
    headline =  soup.select('article > div.story-topper.lede.column.eleven-column > h1')[0]
    tiem =  soup.select('.publish-date > lit-timestamp')[0]
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('.primary-content > :not(p)'):
        s.extract()
    for s in soup.select('.primary-content > :contains("The business website is www.vitalitybowls.com. Choose the Pickerington location once there. The business is also present on Facebook and Instagram.") ~ p'):
        s.extract()
    for s in soup.select('.primary-content > :contains("The business website is www.vitalitybowls.com. Choose the Pickerington location once there. The business is also present on Facebook and Instagram.")'):
        s.extract()
    content =  soup.select('.primary-content')[0]
    
article("https://eu.lancastereaglegazette.com/story/news/2021/11/10/local-restaurant-vitality-bowls-superfood-cafe-expands-menu-options/6336354001/")

urls = [
    "https://www.newburytoday.co.uk/"
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
    #subheadline =  soup.select('#ColLeft > h2')[0]
    for s in soup.select('.review__main-content__section > :not(p,.twitter-tweet )'):
        s.extract()
    for s in soup.select('img'):
        s.extract()
    bodyCopy =  soup.select('.pagestory')[0]
    print(bodyCopy)
article("https://www.newburytoday.co.uk/my-newbury/police-appeal-for-help-after-victim-left-with-facial-injurie-9224614/")
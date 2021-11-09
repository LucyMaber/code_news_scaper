urls = [
    "https://www.coventrytelegraph.net/"
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
    subheadline =  soup.select('[itemprop="description"]')[0]
    for s in soup.select('[itemprop="articleBody"] > :not(p)'):
        s.extract()
    for s in soup.select('[itemprop="articleBody"] > p:contains("Read more")'):
        s.extract()
    for s in soup.select('[itemprop="articleBody"] > p:contains("Keep up with the latest news with our email alerts directly to your inbox")'):
        s.extract()
    for s in soup.select('img'):
        s.extract()
    for s in soup.select('script'):
        s.extract()
    bodyCopy =  soup.select('[itemprop="articleBody"]')[0] ### READ THE FULL STORY
    print(bodyCopy)
article("https://www.coventrytelegraph.net/in-your-area/warning-three-different-roadworks-hit-22101509")


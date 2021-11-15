Q ='[[wikidata:Q5003258]]'
urls = [
    "https://www.buxtonadvertiser.co.uk/"
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
    hedding =  soup.select('article > h1') [0]
    publishedTime =  soup.select('amp-timeago') [0]
    for s in soup.select('a[href="#"] > span'):
        s.extract()
    by =  soup.select('a[href="#"]') [0]
    tags =  soup.select('.article-tag') [0]
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('#content-wrapper >div:not(.markup)'):
        s.extract()
    for s in soup.select('#content-wrapper >h3'):
        s.extract()
    for s in soup.select('#content-wrapper>div:has(p > i)'):
        s.extract()
    article_body =  soup.select_one('#content-wrapper')
    
article("https://www.buxtonadvertiser.co.uk/health/coronavirus/christmas-will-be-lockdown-free-despite-high-case-numbers-boris-johnson-says-3439055")
#frameInner > article > div.sc-bmyXtO.darZld > div.sc-jtggT.iedqFq > div:nth-child(2)

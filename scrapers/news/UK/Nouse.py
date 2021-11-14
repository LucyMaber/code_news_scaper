Q ='[[wikidata:Q7063931]]'
urls = [
    "https://nouse.co.uk/"
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
    headline =  soup.select('header.details-header > h2')[0]
    subheadline =  soup.select('header.details-header > h4')[0]
    for s in soup.select('#articleText > :not(p)'):
        s.extract()
    for s in soup.select('img'):
        s.extract()
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('#articleText > p:contains("Links to support:") ~ p'):
        s.extract()
    for s in soup.select('#articleText > p:contains("Links to support:")'):
        s.extract()
    bodyCopy =  soup.select('#articleText')[0] ### READ THE FULL STORY
    
article("https://nouse.co.uk/2021/04/10/the-last-taboo-releases-report-on-universitys-actions-towards-sexual-assault-and-harassment-")

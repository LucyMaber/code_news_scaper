Q ='[[wikidata:Q5399665]]'
urls = [
    "https://www.essexlive.news/"
]
feeds = [
    "https://www.essexlive.news/rss.xml"
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
    #headline =  soup.select('[itemprop="headline name"]')[0]
    description =  soup.select('[itemprop="description"]')[0]
    #by =   soup.select(".author > .publication-theme")[0]
    datePublished =   soup.select('[itemprop="datePublished"]')[0]
    for s in soup.select('script'):
        s.extract()
    bodyCopy =  soup.select(".p402_hide")[0]
    
async def scan():
    return False
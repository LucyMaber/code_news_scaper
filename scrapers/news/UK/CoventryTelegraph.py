Q ='[[wikidata:Q5179118]]'
urls = [
    "https://www.counselmagazine.co.uk/"
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
    # Need to add author
    title =  soup.select('h1.headline ')[0]
    # subtitle =  soup.select('[itemprop="description"]')[0]
    articleBody =  soup.select('.p402_hide')[0]
    #author =  soup.select('.author > a')[0]
    time =  soup.select('.article-timestamp')[0]
    # description =  soup.select('[itemprop="description"]')[0]
    #title =  soup.select('h1')[0]
    for s in soup.select("script"):
        s.extract()
    
async def scan():
    return False
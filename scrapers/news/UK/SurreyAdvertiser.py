Q ='[[wikidata:Q7646767]]'
urls = [
    "https://www.getsurrey.co.uk/"
]
feeds = [
    "https://www.getsurrey.co.uk/rss.xml"
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
    #time =  soup.select("article > time")[0]
    for s in soup.select('script'):
        s.extract() #p
    for s in soup.select('[itemprop="articleBody"] >  :not(p)'):
        s.extract()
    for s in soup.select('[itemprop="articleBody"] >  :contains("Read more:")'):
        s.extract()
    for s in soup.select('[itemprop="articleBody"] >  :contains("Download the SurreyLive app for a better reader experience and to get news from the areas you care most about. Download it via the ")'):
        s.extract()
    bodyCopy =  soup.select('[itemprop="articleBody"]')[0]
    
article("https://www.getsurrey.co.uk/news/surrey-news/surrey-woman-49-claims-spiked-22111819")
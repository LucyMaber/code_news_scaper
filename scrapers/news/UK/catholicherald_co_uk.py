Q ='[[wikidata:Q4672877]]'
urls = [
    "https://catholicherald.co.uk"
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
    # headline = soup.select('h1[itemprop="headline name"]')[0]
    # 
    # description = soup.select('[itemprop="description"]')[0]
    # 
    author =  soup.select('a[href*="https://catholicherald.co.uk/author"]') [0]
    
    datePublished =  soup.select('a[href*="/posts-by-date/?date"]') [0]
    
    for s in soup.select("div.pvc_clear"):
        
        s.extract()
    for s in soup.select("#pvc_stats_337784"):
        
        s.extract()
    for s in soup.select(".pvc-stats-icon"):
        
        s.extract()
    for s in soup.select(".pvc_clear"):
        
        s.extract()
    for s in soup.select(".pvc_stats"):
        
        s.extract()
    articleBody = soup.select('div.pigeon-first-p')[0]
    
    # dateModified = soup.select('[itemprop="dateModified"]')[0]
    # 
async def scan():
    return False
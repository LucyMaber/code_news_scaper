urls = []
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
    # print(headline)
    # description = soup.select('[itemprop="description"]')[0]
    # print(description)
    author =  soup.select('a[href*="https://catholicherald.co.uk/author"]') [0]
    print(author)
    datePublished =  soup.select('a[href*="/posts-by-date/?date"]') [0]
    print(datePublished)
    for s in soup.select("div.pvc_clear"):
        print("test")
        s.extract()
    for s in soup.select("#pvc_stats_337784"):
        print("test")
        s.extract()
    for s in soup.select(".pvc-stats-icon"):
        print("test")
        s.extract()
    for s in soup.select(".pvc_clear"):
        print("test")
        s.extract()
    for s in soup.select(".pvc_stats"):
        print("test")
        s.extract()
    articleBody = soup.select('div.pigeon-first-p')[0]
    print(articleBody)
    # dateModified = soup.select('[itemprop="dateModified"]')[0]
    # print(dateModified)
article("https://catholicherald.co.uk/traditionalist-group-granted-formal-status-within-the-church-after-a-four-year-wait/")
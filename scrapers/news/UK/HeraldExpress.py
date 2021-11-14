urls = [
    "https://www.devonlive.com/"
]
feeds = [
    "https://www.devonlive.com/rss.xml"
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
    description =  soup.select('[itemprop="description"]')[0]
    datePublished =  soup.select('.date-published')[0]
    dateUpdated =  soup.select('.date-updated')[0]
    try:
        tags = soup.select('[itemprop="keywords"]')[0]
    except:
        pass
    for s in soup.select('[itemprop="articleBody"] > :not(p)'):
        s.extract()
    article =  soup.select('[itemprop="articleBody"]')[0]
    
article("https://www.devonlive.com/news/uk-world-news/woman-spiked-night-out-friends-6171468")
### NEED JAVASCRIPT
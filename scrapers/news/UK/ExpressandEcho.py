Q =''

urls = [
    "https://www.devonlive.com/"
]
feeds = [
"https://www.devonlive.com/all-about/barnstaple/?service=rss",
"https://www.devonlive.com/all-about/bideford/?service=rss",
"https://www.devonlive.com/all-about/brixham/?service=rss",
"https://www.devonlive.com/all-about/crediton/?service=rss",
"https://www.devonlive.com/all-about/cullompton/?service=rss",
"https://www.devonlive.com/all-about/dartmoor/?service=rss",
"https://www.devonlive.com/all-about/dawlish/?service=rss",
"https://www.devonlive.com/all-about/exeter/?service=rss",
"https://www.devonlive.com/all-about/exmoor/?service=rss",
"https://www.devonlive.com/all-about/exmouth/?service=rss",
"https://www.devonlive.com/all-about/honiton/?service=rss",
"https://www.devonlive.com/all-about/ilfracombe/?service=rss",
"https://www.devonlive.com/all-about/newton-abbot/?service=rss",
"https://www.devonlive.com/all-about/northam/?service=rss",
"https://www.devonlive.com/all-about/okehampton/?service=rss",
"https://www.devonlive.com/all-about/paignton/?service=rss",
"https://www.devonlive.com/all-about/plymouth/?service=rss",
"https://www.devonlive.com/all-about/sidmouth/?service=rss",
"https://www.devonlive.com/all-about/tavistock/?service=rss",
"https://www.devonlive.com/all-about/teignmouth/?service=rss",
"https://www.devonlive.com/all-about/tiverton/?service=rss",
"https://www.devonlive.com/all-about/torbay/?service=rss",
"https://www.devonlive.com/all-about/totnes/?service=rss",
"https://www.devonlive.com/all-about/torquay/?service=rss",
"https://www.devonlive.com/news/?service=rss",
"https://www.devonlive.com/news/devon-news/?service=rss",
"https://www.devonlive.com/news/local-news/?service=rss",
"https://www.devonlive.com/all-about/traffic-travel/?service=rss",
"https://www.devonlive.com/all-about/crime/?service=rss",
"https://www.devonlive.com/all-about/education/?service=rss",
"https://www.devonlive.com/news/health/?service=rss",
"https://www.devonlive.com/all-about/politics/?service=rss",
"https://www.devonlive.com/news/jobs/?service=rss",
"https://www.devonlive.com/news/history/?service=rss",
"https://www.devonlive.com/news/celebs-tv/?service=rss",
"https://www.devonlive.com/news/property/?service=rss",
"https://www.devonlive.com/news/motoring/?service=rss",
"https://www.devonlive.com/news/uk-world-news/?service=rss",
"https://www.devonlive.com/all-about/farming/?service=rss",
"https://www.devonlive.com/all-about/environment/?service=rss",
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
    headline =      soup.select('[itemprop="headline name"]')[0]
    description =   soup.select('[itemprop="description"]')[0]
    #dateModified =  soup.select('time')[0]
    for s in soup.select('figure'):
        s.extract()
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('[data-content-type="news"]'):
        s.extract()
    for s in soup.select('[data-link-tracking="InArticle|Link"]'):
        s.extract()
    for s in soup.select('i:contains("Read more:")'):
        s.extract()
    for s in soup.select('i:contains("straight to your inbox by signing up to our daily newsletters")'):
        s.extract()
    articleBody =  soup.select('[itemprop="articleBody"]')[0]
    
async def scan():
    return False
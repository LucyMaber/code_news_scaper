Q ='[[wikidata:Q4923252]]'
urls = [
    "https://www.business-live.co.uk/"
]
feeds = [
"https://www.business-live.co.uk/all-about/west-midlands/?service=rss",
"https://www.business-live.co.uk/all-about/east-midlands/?service=rss",
"https://www.business-live.co.uk/all-about/south-west/?service=rss",
"https://www.business-live.co.uk/all-about/north-west/?service=rss",
"https://www.business-live.co.uk/all-about/north-east/?service=rss",
"https://www.business-live.co.uk/all-about/yorkshire-/umber/?service=rss ",
"https://www.business-live.co.uk/all-about/south-east/?service=rss ",
"https://www.business-live.co.uk/all-about/east/?service=rss ",
"https://www.business-live.co.uk/all-about/lond/n/?service=rss ",
"https://www.business-live.co.uk/all-about/northe/n-ireland/?service=rss ",
"https://www.business-live.co.uk/all-about/wales/?service=rss ",
"https://www.business-live.co.uk/all-about/brexi/?service=rss ",
"https://www.business-live.co.uk/enterprise/?service=rss ",
"https://www.business-live.co.uk/professional-services/?service=rss ",
"https://www.business-live.co.uk/retail-consumer/?service=rss ",
"https://www.business-live.co.uk/economic-development/?service=rss ",
"https://www.business-live.co.uk/technology/?service=rss ",
"https://www.business-live.co.uk/commercial-property/?service=rss ",
"https://www.business-live.co.uk/manufacturing/?service=rss",
"https://www.business-live.co.uk/ports-logistics/?service=rss ",
"https://www.business-live.co.uk/opinion-analysis/?service=rss",
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
    headline =  soup.select_one('[itemprop="headline name"]')
    description =  soup.select_one('[itemprop="description"]')
    author =  soup.select_one(".publication-theme")
    published =  soup.select_one("time.date-published")
    updated =  soup.select_one("time.date-updated")
    #subheadline =  soup.select('article > h2')
    #for s in soup.select('#content-wrapper >div:not(.markup)'):
    #    s.extract()
    for s in soup.select('.ad-placeholder'):
        s.extract()
    for s in soup.select('[itemprop="articleBody"] > section'):
        s.extract()
    for s in soup.select('[itemprop="articleBody"] > h3'):
        s.extract()
    for s in soup.select('script'):
        s.extract()
    for s in soup.select("p:has(b)"):
        s.extract()
    article_body =  soup.select_one('[itemprop="articleBody"]')
    
async def scan():
    return False
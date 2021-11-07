urls = [
    "https://www.hulldailymail.co.uk/"
]
feeds = [
    "https://www.hulldailymail.co.uk/rss.xml"
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
    dateModified =  soup.select('[itemprop="dateModified"]')[0]
    author =  soup.select('[rel="author"]')[0]
    try:
        tags = soup.select('[itemprop="keywords"]')[0]
    except:
        pass
    # for s in soup.select('.article-wrapper > :not(p,b,h1,h2,h3,h4,h5,h6,strong)'):
    #     s.extract()
    for s in soup.select('[itemprop="articleBody"] > :not(p, h1,h2,h3,h4,h5,h6) '):
        s.extract()
    for s in soup.select('p:has(a[data-link-tracking="InArticle|Link"])'):
        s.extract()
    article =  soup.select('[itemprop="articleBody"]')[0]
    print(article)
article("https://www.hulldailymail.co.uk/special-features/win-dream-christmas-25000-won-6156424")
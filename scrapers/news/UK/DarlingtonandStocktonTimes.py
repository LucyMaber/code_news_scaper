urls = [
    "https://www.darlingtonandstocktontimes.co.uk/"
]
feeds = [
    "https://www.darlingtonandstocktontimes.co.uk/news/rss/",
    "https://www.darlingtonandstocktontimes.co.uk/sport/rss/",
    "https://www.darlingtonandstocktontimes.co.uk/opinion/rss/",
    "https://www.darlingtonandstocktontimes.co.uk/opinion/letters/rss/",
    "https://www.darlingtonandstocktontimes.co.uk/farming/rss/",
    "https://www.darlingtonandstocktontimes.co.uk/business/rss/",
    "https://www.darlingtonandstocktontimes.co.uk/lookingback/rss/",
    "https://www.darlingtonandstocktontimes.co.uk/cars/news/rss/",
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
    headline =  soup.select('h1.headline ')[0]
    # description =  soup.select('[itemprop="description"]')[0]
    # dateModified =  soup.select('[itemprop="dateModified"]')[0]
    # by =  soup.select('.publication-theme')[0]
    time =  soup.select('[itemprop="datePublished"]')[0]
    for s in soup.select('script'):
        s.extract()
    bodyCopy =  soup.select('.p402_hide')[0]
    print(bodyCopy)
article("https://www.darlingtonandstocktontimes.co.uk/news/19689944.battling-win-sees-guisborough-rufc-go-nine-points-clear-top-division-two/")

urls = [
    "https://www.lancs.live/"
]
feeds = [
    "https://www.lancs.live/rss.xml"
]
header={
    'sec-ch-ua': 'Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': 'Linux',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
}
from bs4 import BeautifulSoup
import requests
from markdownify import markdownify as md

def article(url):
    print(url)
    content = requests.get(url,headers=header).content
    soup = BeautifulSoup(content, 'html.parser')
    # headline = soup.select('h1[itemprop="headline name"]')[0]
    # print(headline)
    # description = soup.select('[itemprop="description"]')[0]
    # print(description)
    for s in soup.select("p:has(b)"):
        s.extract()
    for s in soup.select("p:-soup-contains('Download the LancsLive app for free on')"):
        print("Download the LancsLive app for")
        s.extract()
    for s in soup.select("p:-soup-contains('To keep updated, follow LancsLive on Facebook and')"):
        print("To keep updated, follow LancsLive on Facebook and")
        s.extract()
    for s in soup.select("p:-soup-contains('To keep updated, follow LancsLive on Facebook and')"):
        print("To keep updated, follow LancsLive on Facebook and")
        s.extract()
    for s in soup.select("p:-soup-contains(' got news for us? Contact our newsdesk')"):
        print("got news for us? Contact our newsdesk")
        s.extract()
    for s in soup.select("p:has(b:-soup-contains(' all the latest news, sport and what's on stories sent to your inbox'))"):
        print(" all the latest news, sport and what's on stories sent to your inbox")
        s.extract()
    for s in soup.select("[data-mod='renderRecommendation']"):
        print("data-mod='renderRecommendation")
        s.extract()
    for s in soup.select("[data-embed-group='read-more']"):
        print("data-embed-group='read-more")
        s.extract()
    for s in soup.select("[data-mod='htmlEmbed']"):
        print("data-mod='htmlEmbed")
        s.extract()
    articleBody = soup.select('[itemprop="articleBody"]')[0]
    print(articleBody)
    author = soup.select('[itemprop="author"]')[0]
    print(author)
    datePublished = soup.select('[itemprop="datePublished"]')[0]
    print(datePublished)
    dateModified = soup.select('[itemprop="dateModified"]')[0]
    print(dateModified)


article("https://www.lancs.live/news/lancashire-news/met-office-weather-forecast-blackpool-22030978")
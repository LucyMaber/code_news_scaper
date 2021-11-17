feeds = [
    "https://www.kentonline.co.uk/_api/rss/kent_online_news_feed.xml",
    "https://www.kentonline.co.uk/_api/rss/dartford_messenger_news_feed.xml",
    "https://www.kentonline.co.uk/_api/rss/east_kent_mercury_news_feed.xml",
    "https://www.kentonline.co.uk/_api/rss/east_kent_mercury_news_feed.xml",
    "https://www.kentonline.co.uk/_api/rss/folkestone_express_sport_feed.xml",
    "https://www.kentonline.co.uk/_api/rss/gillingham_fc_news_feed.xml",
    "https://www.kentonline.co.uk/_api/rss/gravesend_messenger_news_feed.xml",
    "https://www.kentonline.co.uk/_api/rss/kentish_express_news_feed.xml",
    "https://www.kentonline.co.uk/_api/rss/kentish_gazette_news_feed.xml",
    "https://www.kentonline.co.uk/_api/rss/kent_messenger_news_feed.xml",
    "https://www.kentonline.co.uk/_api/rss/medway_messenger_news_feed.xml",
    "https://www.kentonline.co.uk/_api/rss/sittingbourne_messenger_news_feed.xml",
    "https://www.kentonline.co.uk/_api/rss/thanet_extra_news_feed.xml",
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
    headline =  soup.select("h1")[0]
    tag =  soup.select(".CatKey ")[0]
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('.PageContent > .PageStory > :not(p)'):
        s.extract()
    for s in soup.select('.PageContent > .PageStory > p:contains("Read more")'):
        s.extract()
    for s in soup.select('.PageContent > .PageStory > p:contains("Cosgrove Leisure was approached")'):
        s.extract()
    # for s in soup.select('div[class="article__detail-text mdc-typography--body1" > script'):
    #     s.extract()
    bodyCopy =  soup.select('.PageContent > .PageStory')[0]
    
async def scan():
    return False
Q ='[[wikidata:Q7861589]]'
urls = [
    "https://www.tyronecourier.co.uk/"
]
feeds = [
"https://www.glasgowtimes.co.uk/news/rss/",
"https://www.glasgowtimes.co.uk/news/glasgow-crime/rss/",
"https://www.glasgowtimes.co.uk/news/councilandpoliics/rss/",
"https://www.glasgowtimes.co.uk/news/councilandpoliics/rss/",
"https://www.glasgowtimes.co.uk/news/health/rss/",
"https://www.glasgowtimes.co.uk/news/planning-development/rss/",
"https://www.glasgowtimes.co.uk/news/glasgow-city-centre/rss/",
"https://www.glasgowtimes.co.uk/news/glasgow-southside/rss/",
"https://www.glasgowtimes.co.uk/news/glasgow-east-end/rss/",
"https://www.glasgowtimes.co.uk/news/north-glasgow/rss/",
"https://www.glasgowtimes.co.uk/news/best-of/rss/",
"https://www.glasgowtimes.co.uk/sport/glasgowclan/rss/",
"https://www.glasgowtimes.co.uk/sport/glasgow-warriors/rss/",
"https://www.glasgowtimes.co.uk/news/north-glasgow/rss/",
"https://www.glasgowtimes.co.uk/lifestyle/nostalgia/rss/",
"https://www.glasgowtimes.co.uk/lifestyle/fashion/rss/",
"https://www.glasgowtimes.co.uk/lifestyle/expert_advice/rss/",
"https://www.glasgowtimes.co.uk/lifestyle/spring-in-the-city/rss/",
"https://www.glasgowtimes.co.uk/lifestyle/homes/rss/",
"https://www.glasgowtimes.co.uk/opinion/columnists/rss/",
"https://www.glasgowtimes.co.uk/opinion/letters/rss/",
"https://www.glasgowtimes.co.uk/opinion/et_view/rss/",
"https://www.glasgowtimes.co.uk/campaigns/streets-ahead/rss/",
"https://www.glasgowtimes.co.uk/campaigns/community-champs/rss/",
"https://www.glasgowtimes.co.uk/campaigns/scotswoman-of-the-year/rss/",
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
    headline =  soup.select('h1[itemprop="headline name"] ')[0]
    # time =  soup.select('#native-content-pub-date')[0]
    for s in soup.select('img'):
        s.extract()
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('figure'):
        s.extract()
    for s in soup.select('[itemprop="text"] > p:contains("Full stories and photos in this week\'s Courier.")'):
        s.extract()
    for s in soup.select('[itemprop="text"] > p:contains("Click here for Digital ePaper")'):
        s.extract()
    bodyCopy =  soup.select('[itemprop="text"]')[0]
    
async def scan():
    return False
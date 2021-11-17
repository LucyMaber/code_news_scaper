Q =''
urls = [
    "https://www.bbc.co.uk/"
]
feeds = [
"http://feeds.bbci.co.uk/news/rss.xml",
"http://feeds.bbci.co.uk/news/world/rss.xml",
"http://feeds.bbci.co.uk/news/uk/rss.xml",
"http://feeds.bbci.co.uk/news/politics/rss.xml",
"http://feeds.bbci.co.uk/news/business/rss.xml",
"http://feeds.bbci.co.uk/news/health/rss.xml",
"http://feeds.bbci.co.uk/news/education/rss.xml",
"http://feeds.bbci.co.uk/news/science_and_environment/rss.xml",
"http://feeds.bbci.co.uk/news/technology/rss.xml",
"http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml",
"http://feeds.bbci.co.uk/news/world/africa/rss.xml",
"http://feeds.bbci.co.uk/news/world/asia/rss.xml",
"http://feeds.bbci.co.uk/news/world/europe/rss.xml",
"http://feeds.bbci.co.uk/news/world/middle_east/rss.xml",
"http://feeds.bbci.co.uk/news/world/us_and_canada/rss.xml",
"http://feeds.bbci.co.uk/news/northern_ireland/rss.xml",
"http://feeds.bbci.co.uk/news/scotland/rss.xml",
"http://feeds.bbci.co.uk/news/wales/rss.xml",
"http://feeds.bbci.co.uk/news/video_and_audio/news_front_page/rss.xml?edition=uk",
"http://feeds.bbci.co.uk/news/video_and_audio/world/rss.xml",
"http://feeds.bbci.co.uk/news/system/latest_published_content/rss.xml",
"http://feeds.bbci.co.uk/news/magazine/rss.xml",
"http://feeds.bbci.co.uk/news/also_in_the_news/rss.xml",
"http://feeds.bbci.co.uk/news/special_reports/rss.xml",
"http://feeds.bbci.co.uk/news/have_your_say/rss.xml",
"https://www.bbc.co.uk/blogs/theeditors/rss.xml",
"https://news.bbc.co.uk/sport1/hi/help/rss/default.stm",
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
    # Need to add author
    headline =  soup.select('#main-heading') [0]
    time =  soup.select('time[data-testid="timestamp"]')
    for s in soup.select('[data-component="see-alsos"]'):
        s.extract()
    for s in soup.select('[data-component="tag-list"]'):
        s.extract()
    for s in soup.select('[data-component="image-block"]'):
        s.extract()
    for s in soup.select('[data-component="unordered-list-block"]'):
        s.extract()
    for s in soup.select('[data-component="include-block"]'):
        s.extract()
    for s in soup.select('[data-component="crosshead-block"]'):
        s.extract()
    for s in soup.select('[data-component="unordered-list-block"]'):
        s.extract()
    for s in soup.select('header'):
        s.extract()
    
async def scan():
    return False
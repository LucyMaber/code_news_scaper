urls = [
    "https://www.thenonleaguefootballpaper.com/"
]
feeds = [
    "https://www.thenonleaguefootballpaper.com/feed/",
    "https://www.thenonleaguefootballpaper.com/comments/feed/"
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
    headline =  soup.select('.entry-title')[0]
    time =  soup.select('time.entry-date')[0]
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('img'):
        s.extract()
    for s in soup.select('[class="entry-content"] > :not(p)'):
        s.extract()
    content =  soup.select('[class="entry-content"]')[0]
    print(content)
article("https://www.thenonleaguefootballpaper.com/latest-news/step-1/national-league/412892/the-nl-full-time-podcast-3/")

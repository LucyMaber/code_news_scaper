urls = [
    "https://www.somersetlive.co.uk/all-about/bath"
]
feeds = [
    "https://www.somersetlive.co.uk/rss.xml"
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
    article_body =  soup.select("[itemprop='articleBody']")
    for s in soup.select("script"):
        s.extract()
    headline =  soup.select('[itemprop="headline name"]')
    
article("https://www.somersetlive.co.uk/news/somerset-news/girl-14-suffered-head-injury-6142049/")
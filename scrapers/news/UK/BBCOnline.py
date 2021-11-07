urls = [
    "https://www.bbc.co.uk/"
]
feeds = [

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
    print(headline)
article("https://www.bbc.co.uk/news/science-environment-59088498")
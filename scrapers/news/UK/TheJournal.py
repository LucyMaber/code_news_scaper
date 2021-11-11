urls = [
    "https://www.thejournal.ie/"
]
feeds = [
    "https://www.thejournal.ie/feed/"
]
header={
    # 'sec-ch-ua': 'Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': 'Linux',
    # 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
}


from bs4 import BeautifulSoup
import requests

def article(url):
    req = requests.get(url,headers=header)
    content = req.content
    soup = BeautifulSoup(content, 'html.parser')
    headline =  soup.select('[itemprop="headline"]')[0]
    subheadline =  soup.select('[itemprop="description"]')[0]
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('.article-updated'):
        s.extract()
    for s in soup.select('#contribution-prompt-article'):
        s.extract()
    content =  soup.select('#articleContent')[0]
    print(content)
article("https://www.thejournal.ie/tony-holohan-cut-socialising-by-half-covid-19-5597460-Nov2021/")

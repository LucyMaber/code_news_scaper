Q ='[[wikidata:Q10991471]]'
urls = [
    "https://www.morningstar.co.uk/"
]
feeds = [
    "https://www.morningstar.co.uk/uk/feeds/rss.aspx?lang=en-GB"
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
    headline =  soup.select('#ColLeft > h1')[0]
    #subheadline =  soup.select('#ColLeft > h2')[0]
    for s in soup.select('#changefont > div'):
        s.extract()
    for s in soup.select('img'):
        s.extract()
    bodyCopy =  soup.select('#changefont')[0]
    
article("https://www.morningstar.co.uk/uk/news/216636/cop26-big-banks-and-climate-change.aspx")

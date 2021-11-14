Q ='[[wikidata:Q610190]]'
urls = [
    "https://www.express.co.uk/"
]

feeds = [
    "https://www.express.co.uk/posts/rss/106/royal"
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
    #headline =  soup.select('h1.headline')
    for s in soup.select('article div.ctx_content.p402_premium div.clearfix.hR.new-style > div:not(.text-description)'):
        s.extract()
    for s in soup.select('article div.ctx_content.p402_premium div.clearfix.hR.new-style > div:not(.text-description)'):
        s.extract()
    for s in soup.select('div.text-description > div > div > div > div > p > strong:contains("FOLLOW LIVE UPDATES BELOW")'):
        s.extract()
    article_body_part =  soup.select('article div.ctx_content.p402_premium div.clearfix.hR.new-style')[0]
    
article("https://www.express.co.uk/news/politics/1515820/PMQs-live-Rayner-Paterson-by-election-Johnson")

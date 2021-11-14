urls = [
    "https://www.newlawjournal.co.uk/"
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
    headline =  soup.select('h1.title')[0]
    time =  soup.select('.postText > span')[0]
    for s in soup.select('.bodyHeadingTag > :not(p)'):
        s.extract()
    bodyCopy =  soup.select('.bodyHeadingTag:has(p)')[0]
    
article("https://www.newlawjournal.co.uk/content/pro-bono-week-behind-the-numbers")

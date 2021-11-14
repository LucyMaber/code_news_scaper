urls = [
    "https://www.anphoblacht.com/"
]
feeds = [
"https://www.anphoblacht.com/feed"
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
    a = soup.select('p.author > span')[0]
    a.extract()
    author =  soup.select('p.author') [0]
    
    edition_title =  soup.select('.edition-title') [0]
    
    articleBody = soup.select('.span5')[0]
    
article("https://www.anphoblacht.com/contents/28198")
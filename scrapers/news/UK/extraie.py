Q =''
urls = [
    "https://extra.ie/"
]
feeds = [
    "https://ansionnachfionn.com/feed/"
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
    headline =  soup.select('h1.entry-title')[0]
    # description =  soup.select('h3.entry-title')[0]
    # author =  soup.select('.author > a')[0]
    # time =  soup.select('.dates > time')[0]
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('input'):
        s.extract()
    for s in soup.select('#jwp-outstream-unit'):
        s.extract()
    articleBody =  soup.select('.td-post-content > div')[0]
    
article("https://extra.ie/2021/11/06/entertainment/full-line-up-of-im-a-celebrity-revealed-as-david-ginola-frankie-bridge-and-soap-legends-set-for-stints")
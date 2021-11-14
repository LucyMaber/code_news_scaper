urls = [
    "https://www.thegryphon.co.uk/"
]
feeds = [
    "https://www.thegryphon.co.uk/feed/",
    "https://www.thegryphon.co.uk/comments/feed/",
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
    article =  soup.select('.entry-content')[0]
    
article("https://www.thegryphon.co.uk/2021/11/08/university-of-leeds-staff-back-strike-over-pay-and-conditions/")

urls = [
    "https://thegoodlifesurbiton.co.uk/"
]
feeds = [
    "https://thegoodlifesurbiton.co.uk/feed/",
    "https://thegoodlifesurbiton.co.uk/feed/"
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
    headline =  soup.select('h1.post_title')[0]
    article =  soup.select('.text')[0]
    
article("https://thegoodlifesurbiton.co.uk/2021/11/03/talk-on-titanic-and-link-with-st-marys-church-long-ditton/")

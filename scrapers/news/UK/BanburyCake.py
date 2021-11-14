Q =''
urls = []
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
    author = soup.select('a[href*="/author/profile/"]') [0]
    article =  soup.select('#subscription-replace-entire-article') [0]
    for s in soup.select("script"):
        s.extract()
    #
    headline =  soup.select('h1.headline ') [0]
    time =  soup.select('time ') [0]
    
article("https://www.banburycake.co.uk/news/19678856.kaleb-cooper-opens-farming-area-banbury-bicester-college/")
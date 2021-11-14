Q =''
urls = [
    "https://www.scidev.net/"
]
feeds = [
    "https://www.scidev.net/global/global_rss.xml"
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
    headline =  soup.select('[class="fl-heading-text"]')[0]
    #time =  soup.select("article > time")[0]
    for s in soup.select('script'):
        s.extract()
    # for s in soup.select('.fl-module-content >:not(p,h1,h2,h3,h4,h5,h6,strong)'):
    #     s.extract()
    # for s in soup.select('.fl-module-content > p:contains("Get more Salisbury news.") ~ p'):
    #     s.extract()
    # for s in soup.select('.fl-module-content > p:contains("Get more Salisbury news.")'):
    #     s.extract()
    bodyCopy =  soup.select('[class="fl-module fl-module-fl-post-content fl-node-5c7e18968ba4f extra-formating scidev-table-responsive"]>[class="fl-module-content fl-node-content"]')[0]
    
article("https://www.scidev.net/global/news/doubt-grows-over-cop26-forest-pledge/")
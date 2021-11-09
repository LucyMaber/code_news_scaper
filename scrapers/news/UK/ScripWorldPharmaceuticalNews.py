urls = [
    "https://scrip.pharmaintelligence.informa.com/"
]
feeds = [
    "https://feeds.feedblitz.com/scrip",
    "https://feeds.feedblitz.com/scrip-regulation",
    "https://feeds.feedblitz.com/scrip-companies",
    "https://feeds.feedblitz.com/scrip-deals",
    "https://feeds.feedblitz.com/scrip-strategy",
    "https://feeds.feedblitz.com/scrip-approvals",
    "https://feeds.feedblitz.com/scrip-clinical-trials",
    "https://feeds.feedblitz.com/scrip-cancer",
    "https://feeds.feedblitz.com/scrip-neurology",
    "https://feeds.feedblitz.com/scrip-orthopedics",
    "https://feeds.feedblitz.com/scrip-infectious-diseases",
    "https://feeds.feedblitz.com/scrip-cardiovascular",
    "https://feeds.feedblitz.com/metabolic-disorders",
    "https://feeds.feedblitz.com/scrip-asia-pacific",
    "https://feeds.feedblitz.com/scrip-europe",
    "https://feeds.feedblitz.com/scrip-north-america",
]
header={
    'sec-ch-ua': 'Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': 'Linux',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
}


from bs4 import BeautifulSoup
import requests

# def article(url):
#     content = requests.get(url,headers=header).content
#     soup = BeautifulSoup(content, 'html.parser')
#     headline =  soup.select('.article-body-content > h1')[0]
#     subheadline =  soup.select('.article-body-content > h2')[0]
#     #time =  soup.select("article > time")[0]
#     for s in soup.select('script'):
#         s.extract()
#     for s in soup.select('article  :not(p,h1,h3,h4,h5,h6,strong)'):
#         s.extract()
#     for s in soup.select('article  figure'):
#         s.extract()
#     bodyCopy =  soup.select('article')[0]
#     print(bodyCopy)
# article("https://socialistvoice.scot/2021/07/31/danny-odonnell/")
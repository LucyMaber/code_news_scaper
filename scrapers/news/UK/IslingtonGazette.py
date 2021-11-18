Q ='[[wikidata:Q6084365]]'
urls = [
    "https://www.islingtongazette.co.uk/"
]
feeds = [
"https://www.manchestereveningnews.co.uk/all-about/bolton/rss.xml",
"https://www.manchestereveningnews.co.uk/all-about/bury/rss.xml",
"https://www.manchestereveningnews.co.uk/all-about/manchester-city-centre/rss.xml",
"https://www.manchestereveningnews.co.uk/all-about/manchester/rss.xml",
"https://www.manchestereveningnews.co.uk/all-about/oldham/rss.xml",
"https://www.manchestereveningnews.co.uk/all-about/manchester-city-centre/rss.xml",
"https://www.manchestereveningnews.co.uk/all-about/mancheste/rss.xml",
"https://www.manchestereveningnews.co.uk/all-about/oldham/rss.xml",
"https://www.manchestereveningnews.co.uk/all-about/rochdale/rss.xml",
"https://www.manchestereveningnews.co.uk/all-about/salford/rss.xml",
"https://www.manchestereveningnews.co.uk/all-about/stockport/rss.xml",
"https://www.manchestereveningnews.co.uk/all-about/tameside/rss.xml",
"https://www.manchestereveningnews.co.uk/all-about/trafford/rss.xml",
"https://www.manchestereveningnews.co.uk/all-about/wigan/rss.xml",
"https://www.manchestereveningnews.co.uk/news/rss.xml",
"https://www.manchestereveningnews.co.uk/news/uk-news/rss.xml",
"https://www.manchestereveningnews.co.uk/all-about/politics/rss.xml",
"https://www.manchestereveningnews.co.uk/all-about/crime/rss.xml",
"https://www.manchestereveningnews.co.uk/news/health/rss.xml",
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
    # for s in soup.select('.article-wrapper > :not(p,b,h1,h2,h3,h4,h5,h6,strong)'):
    #     s.extract()
    for s in soup.select('.entry-content > :not(p, h1,h2,h3,h4,h5,h6) '):
        s.extract()
    article =  soup.select('.entry-content')[0]
    
async def scan():
    return False
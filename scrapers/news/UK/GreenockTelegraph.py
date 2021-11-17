Q =""
urls = [
    "https://www.greenocktelegraph.co.uk/"
]
feeds = [
"https://www.greenocktelegraph.co.uk/news/rss/",
"https://www.greenocktelegraph.co.uk/news/greenock/rss/",
"https://www.greenocktelegraph.co.uk/news/gourock/rss/",
"https://www.greenocktelegraph.co.uk/news/portglasgow/rss/",
"https://www.greenocktelegraph.co.uk/news/villages/rss/",
"https://www.greenocktelegraph.co.uk/news/national-news/rss/",
"https://www.greenocktelegraph.co.uk/news/general-election/rss/",
"https://www.greenocktelegraph.co.uk/news/coronavirus/rss/",
"https://www.greenocktelegraph.co.uk/opinion/rss/",
"https://www.greenocktelegraph.co.uk/opinion/comment/rss/",
"https://www.greenocktelegraph.co.uk/opinion/talkofthetowns/rss/",
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
    headline =  soup.select('h1.headline ')[0]
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('.subscription-content > :not(ul ,p, strong)'):
        s.extract()
    for s in soup.select('p > :contains("READ MORE:")'):
        s.extract()
    for s in soup.select('p > :contains("Get the biggest stories")'):
        s.extract()
    for s in soup.select('p > :contains("please log in and leave you comments below.")'):
        s.extract()
    content =  soup.select('.p402_hide')[0]
    
async def scan():
    return False

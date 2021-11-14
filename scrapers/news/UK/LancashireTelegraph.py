Q ='[[wikidata:Q6483046]]'
urls = [
    "https://www.lancashiretelegraph.co.uk/"
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
    headline =  soup.select("article > h1 ")[0]
    #time =  soup.select("article > time")[0]
    author =  soup.select(".author-name > a")[0]
    for s in soup.select('script'):
        s.extract()
    bodyCopy =  soup.select(".p402_hide")[0]
    
article("https://www.lancashiretelegraph.co.uk/news/19699708.blackburn-darwen-sees-10-per-cent-rise-reports-sexual-offences/")
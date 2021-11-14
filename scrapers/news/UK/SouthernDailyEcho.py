Q ='[[wikidata:Q7569853]]'
urls = [
    "https://www.dailyecho.co.uk/"
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
    headline =  soup.select('.headline')[0]
    # for s in soup.select('.article-wrapper > :not(p,b,h1,h2,h3,h4,h5,h6,strong)'):
    #     s.extract()
    for s in soup.select('#subscription-content > :not(p, h1,h2,h3,h4,h5,h6) '):
        s.extract()
    for s in soup.select('#subscription-content > p:contains("READ MORE")'):
        s.extract()
    for s in soup.select('#subscription-content > p:contains("Want our best stories with fewer ads and alerts when the biggest news stories drop? Download our app")'):
        s.extract()
    for s in soup.select('#subscription-content > p:contains("Get the biggest stories from across")'):
        s.extract()
    for s in soup.select('script'):
        s.extract()
    article =  soup.select('.p402_hide')[0]
    
article("https://www.dailyecho.co.uk/news/19703139.row-plans-mend-southampton-road-not-owned-council/")
Q ='[[wikidata:Q661005]]'
urls = [
    "https://www.thenorthernecho.co.uk/"
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
    #subheadline =  soup.select('article > h2')[0]
    for s in soup.select('.subscription-content > :not(p)'):
        s.extract()
    for s in soup.select('#inArticleAd-2'):
        s.extract()
    for s in soup.select('img'):
        s.extract()
    for s in soup.select('#subscription-content > :not(p)'):
        s.extract()
    for s in soup.select('#subscription-content > p:contains("Read more")'):
        s.extract()
    for s in soup.select('#subscription-content > :contains("Keep up to date with all the latest news on our website, or follow us on ")'):
        s.extract()
    for s in soup.select('#subscription-content > :contains("all the top news updates from ")'):
        s.extract()
    for s in soup.select('#subscription-content > :contains("You can also follow our dedicated Darlington Facebook page for all the latest in the area")'):
        s.extract()
    for s in soup.select('#subscription-content > :contains("Have you got a story for us? Contact our newsdesk on newsdesk@nne.co.uk or contact 01325 505054")'):
        s.extract()
    for s in soup.select('#subscription-content > :contains("For all the top news updates from right")'):
        s.extract()
    for s in soup.select('#subscription-content > :contains("For all the top news updates from right across the region straight to your inbox, sign up to our newsletter ")'):
        s.extract()
    for s in soup.select('.p402_hide > :not(p,#subscription-content)'):
        s.extract()
    bodyCopy =  soup.select('.p402_hide')[0] ### READ THE FULL STORY
    
article("https://www.thenorthernecho.co.uk/news/19703324.data-reveals-darlington-councils-climate-ambitions/")

Q ='[[wikidata:Q5302846]]'
urls = [
    "http://www.thedownrecorder.co.uk/"
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
    headline =  soup.select('h1')[0]
    data =  soup.select('.header_bottom')[0]
    #subheadline =  soup.select('article > h2 ')[0]
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('a:has(img)'):
        s.extract()
    for s in soup.select('h3'):
        s.extract()
    bodyCopy =  soup.select('.cell_right_sub1')[0]
    
article("http://www.thedownrecorder.co.uk/pages/?title=Vandals_target_special_school")
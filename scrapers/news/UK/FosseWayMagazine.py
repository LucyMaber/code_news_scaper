Q =''
urls = [
    "https://www.somersetlive.co.uk/"
]
feeds = [
    "https://www.somersetlive.co.uk/rss.xml"
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
    headline =  soup.select('article > h1')[0]
    description =  soup.select('article > p')[0]
    dateModified =  soup.select('time.date-updated')[0]
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('.live-event-lead-entry > :not(p , h1 , h2 , h3 , h4 , h5 , h6 , h7 , h8 , h9)'):
        s.extract()
    artcal =  soup.select('.live-event-lead-entry')[0]
    

article("https://www.football.london/arsenal-fc/fixtures-results/arsenal-press-conference-live-mikel-22072410")
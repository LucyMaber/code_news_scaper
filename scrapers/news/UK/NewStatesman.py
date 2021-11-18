Q ='[[wikidata:Q1566255]]'
urls = [
    "https://www.newstatesman.com/"
]
feeds = [
    "https://www.newstatesman.com/science-tech/science-of-us/feed",
    "https://www.newstatesman.com/social-media/feed",
    "https://www.newstatesman.com/science-tech/coronavirus/feed",
    "https://www.newstatesman.com/internet/feed",
    "https://www.newstatesman.com/environment/climate/feed",
    "https://www.newstatesman.com/technology/feed",
    "https://www.newstatesman.com/science-tech/feed",
    "https://www.newstatesman.com/environment/feed",
    "https://www.newstatesman.com/environment/just-transition/feed",
    "https://www.newstatesman.com/environment/biodiversity/feed",
    "https://www.newstatesman.com/environment/climate/feed",
    "https://www.newstatesman.com/business/feed",
    "https://www.newstatesman.com/business/work/feed",
    "https://www.newstatesman.com/business/economics/feed",
    "https://www.newstatesman.com/business/sustainability/feed",
    "https://www.newstatesman.com/business/finance/feed",
    "https://www.newstatesman.com/business/sectors/feed",
    "https://www.newstatesman.com/business/companies/feed",
    "https://www.newstatesman.com/spotlight/feed",
    "https://www.newstatesman.com/spotlight/skills/feed",
    "https://www.newstatesman.com/spotlight/emerging-technologies/feed",
    "https://www.newstatesman.com/spotlight/devolution/feed",
    "https://www.newstatesman.com/spotlight/housing/feed",
    "https://www.newstatesman.com/spotlight/energy/feed",
    "https://www.newstatesman.com/spotlight/transport/feed",
    "https://www.newstatesman.com/spotlight/fintech/feed",
    "https://www.newstatesman.com/spotlight/healthcare/feed",
    "https://www.newstatesman.com/spotlight/manufacturing/feed",
    "https://www.newstatesman.com/spotlight/cyber/feed",
    "https://www.newstatesman.com/spotlight/manufacturing/feed",
    "https://www.newstatesman.com/spotlight/healthcare/feed",
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
    headline =  soup.select('.c-article-header__title')[0]
    subheadline =  soup.select('.c-article-excerpt')[0]
    for s in soup.select('.c-article-content__container > :not(p)'):
        s.extract()
    bodyCopy =  soup.select('.c-article-content__container')[0] ### READ THE FULL STORY
    
async def scan():
    return False
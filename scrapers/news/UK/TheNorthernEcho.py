Q ='[[wikidata:Q661005]]'
urls = [
    "https://www.thenorthernecho.co.uk/"
]
feeds = [
    "https://www.thenorthernecho.co.uk/news/rss/",
    "https://www.thenorthernecho.co.uk/news/local/darlington/rss/",
    "https://www.thenorthernecho.co.uk/news/local/darlington/darlingtonboroughcouncil/rss/",
    "https://www.thenorthernecho.co.uk/news/local/countydurham/barnardcastle/rss/",
    "https://www.thenorthernecho.co.uk/news/local/countydurham/barnardcastle/communitynews/rss/",
    "https://www.thenorthernecho.co.uk/news/local/countydurham/bishopauckland/rss/",
    "https://www.thenorthernecho.co.uk/news/local/countydurham/ferryhill/rss/",
    "https://www.thenorthernecho.co.uk/news/local/countydurham/newtonaycliffe/rss/",
    "https://www.thenorthernecho.co.uk/news/local/countydurham/sedgefield/rss/",
    "https://www.thenorthernecho.co.uk/news/local/countydurham/shildon/rss/",
    "https://www.thenorthernecho.co.uk/news/local/countydurham/spennymoor/rss/",
    "https://www.thenorthernecho.co.uk/news/local/countydurham/weardale/rss/",
    "https://www.thenorthernecho.co.uk/news/local/teesside/rss/",
    "https://www.thenorthernecho.co.uk/news/local/teesside/middlesbrough/rss/",
    "https://www.thenorthernecho.co.uk/news/local/teesside/stockton/rss/",
    "https://www.thenorthernecho.co.uk/news/local/teesside/redcar/rss/",
    "https://www.thenorthernecho.co.uk/news/local/teesside/hartlepool/rss/",
    "https://www.thenorthernecho.co.uk/news/local/teesside/hartlepool/communitynews/rss/",
    "https://www.thenorthernecho.co.uk/news/local/teesside/guisborough/rss/",
    "https://www.thenorthernecho.co.uk/news/local/teesside/yarm/rss/",
    "https://www.thenorthernecho.co.uk/news/local/northyorkshire/rss/",
    "https://www.thenorthernecho.co.uk/news/local/northdurham/rss/",
    "https://www.thenorthernecho.co.uk/news/politics/rss/",
    "https://www.thenorthernecho.co.uk/news/crime/rss/",
    "https://www.thenorthernecho.co.uk/news/health/rss/",
    "https://www.thenorthernecho.co.uk/news/health/features/rss/",
    "https://www.thenorthernecho.co.uk/news/council/darlingtonboroughcouncil/rss/",
    "https://www.thenorthernecho.co.uk/news/council/durhamcountycouncil/rss/",
    "https://www.thenorthernecho.co.uk/news/council/middlesbroughcouncil/rss/",
    "https://www.thenorthernecho.co.uk/news/council/stocktonboroughcouncil/rss/",
    "https://www.thenorthernecho.co.uk/news/council/hartlepoolboroughcouncil/rss/",
    "https://www.thenorthernecho.co.uk/news/council/redcarandclevelandboroughcouncil/rss/",
    "https://www.thenorthernecho.co.uk/news/council/northyorkshirecountycouncil/rss/",
    "https://www.thenorthernecho.co.uk/news/todayupnorth/rss/",
    "https://www.thenorthernecho.co.uk/news/todayupnorth/features/rss/",
    "https://www.thenorthernecho.co.uk/news/todayupnorth/business/rss/",
    "https://www.thenorthernecho.co.uk/news/todayupnorth/education/rss/",
    "https://www.thenorthernecho.co.uk/opinion/rss/",
    "https://www.thenorthernecho.co.uk/opinion/letters/rss/",
    "https://www.thenorthernecho.co.uk/opinion/columnists/rss/",
    "https://www.thenorthernecho.co.uk/opinion/columnists/hannahchapman/rss/",
    "https://www.thenorthernecho.co.uk/opinion/columnists/mikeamos/rss/",
    "https://www.thenorthernecho.co.uk/opinion/columnists/chrislloyd/rss/",
    "https://www.thenorthernecho.co.uk/opinion/columnists/peterbarron/rss/",
    "https://www.thenorthernecho.co.uk/opinion/columnists/peterbarron/rss/",
    "https://www.thenorthernecho.co.uk/opinion/columnists/dadatlarge/rss/",
    "https://www.thenorthernecho.co.uk/opinion/columnists/arunarora/rss/",
    "https://www.thenorthernecho.co.uk/opinion/comment/rss/",
    "https://www.thenorthernecho.co.uk/news/national/rss/",
    "https://www.thenorthernecho.co.uk/news/national/uk-today/rss/"
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
    
async def scan():
    return False
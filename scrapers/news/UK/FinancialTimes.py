Q ='[[wikidata:Q183399]]'
urls = [
    "https://www.ft.com/"
]
feeds = [
"https://www.ft.com/global-economy?format=rss",
"https://www.ft.com/world/uk?format=rss",
"https://www.ft.com/world/us?format=rss",
"https://www.ft.com/world/asia-pacific/china?format=rss",
"https://www.ft.com/world/africa?format=rss",
"https://www.ft.com/world/asia-pacific?format=rss",
"https://www.ft.com/emerging-markets?format=rss",
"https://www.ft.com/world/americas?format=rss",
"https://www.ft.com/world/europe?format=rss",
"https://www.ft.com/world/mideast?format=rss",
"https://www.ft.com/companies/energy?format=rss",
"https://www.ft.com/companies/financials?format=rss",
"https://www.ft.com/companies/health?format=rss",
"https://www.ft.com/companies/industrials?format=rss",
"https://www.ft.com/companies/media?format=rss",
"https://www.ft.com/companies/professional-services?format=rss",
"https://www.ft.com/companies/retail-consumer?format=rss",
"https://www.ft.com/companies/technology?format=rss",
"https://www.ft.com/companies/telecoms?format=rss",
"https://www.ft.com/companies/transport?format=rss",
"https://www.ft.com/technology?format=rss",
"https://www.ft.com/alphaville?format=rss",
"https://www.ft.com/capital-markets?format=rss",
"https://www.ft.com/commodities?format=rss",
"https://www.ft.com/equities?format=rss",
"https://www.ft.com/fund-management?format=rss",
"https://www.ft.com/ft-trading-room?format=rss",
"https://www.ft.com/moral-money?format=rss",
"https://www.ft.com/cryptocurrencies?format=rss",
"https://www.ft.com/markets?format=rss",
"https://www.ft.com/climate-capital?format=rss",
"https://www.ft.com/columnists?format=rss",
"https://www.ft.com/ft-view?format=rss",
"https://www.ft.com/the-big-read?format=rss",
"https://www.ft.com/lex?format=rss",
"https://www.ft.com/obituaries?format=rss",
"https://www.ft.com/letters?format=rss",
"https://www.ft.com/opinion?format=rss",
"https://www.ft.com/business-education?format=rss",
"https://www.ft.com/entrepreneurship?format=rss",
"https://www.ft.com/recruitment?format=rss",
"https://www.ft.com/business-books?format=rss",
"https://www.ft.com/business-travel?format=rss",
"https://www.ft.com/work-careers?format=rss",
"https://www.ft.com/arts?format=rss",
"https://www.ft.com/books?format=rss",
"https://www.ft.com/food-drink?format=rss",
"https://www.ft.com/magazine?format=rss",
"https://www.ft.com/house-home?format=rss",
"https://www.ft.com/style?format=rss",
"https://www.ft.com/travel?format=rss",
"https://www.ft.com/globetrotter?format=rss",
"https://www.ft.com/life-arts?format=rss",
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
    headline =  soup.select('[itemprop="headline"]')[0]
    description =  soup.select('[itemprop="description"]')[0]
    # description =  soup.select('h3.entry-title')[0]
    # author =  soup.select('.author > a')[0]
    # time =  soup.select('.dates > time')[0]
    #for s in soup.select('script'):
        #s.extract()
    #PAY WALL
async def scan():
    return False
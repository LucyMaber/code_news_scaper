Q ='Q64356086'
urls = [
    "https://www.lancashiretelegraph.co.uk/"
]
feeds = [
    "https://www.lancashiretelegraph.co.uk/news/rss/",
    "https://www.lancashiretelegraph.co.uk/sport/rss/",
    "https://www.lancashiretelegraph.co.uk/news/blackburn/rss/",
    "https://www.lancashiretelegraph.co.uk/news/burnley/rss/",
    "https://www.lancashiretelegraph.co.uk/news/burnley/briercliffe/rss/",
    "https://www.lancashiretelegraph.co.uk/news/burnley/cliviger/rss/",
    "https://www.lancashiretelegraph.co.uk/news/burnley/hapton/rss/",
    "https://www.lancashiretelegraph.co.uk/news/burnley/rosegrove/rss/",
    "https://www.lancashiretelegraph.co.uk/news/burnley/worsthorne/rss/",
    "https://www.lancashiretelegraph.co.uk/news/darwen/rss/",
    "https://www.lancashiretelegraph.co.uk/news/darwen/hoddlesden/rss/",
    "https://www.lancashiretelegraph.co.uk/news/darwen/tockholes/rss/",
    "https://www.lancashiretelegraph.co.uk/news/darwen/sam_shaw_appeal/rss/",
    "https://www.lancashiretelegraph.co.uk/news/darwen/northturton/rss/",
    "https://www.lancashiretelegraph.co.uk/news/ribble_valley/rss/",
    "https://www.lancashiretelegraph.co.uk/news/ribble_valley/billington/rss/",
    "https://www.lancashiretelegraph.co.uk/news/ribble_valley/chipping/rss/",
    "https://www.lancashiretelegraph.co.uk/news/ribble_valley/clitheroe/rss/",
    "https://www.lancashiretelegraph.co.uk/news/ribble_valley/gisburn/rss/",
    "https://www.lancashiretelegraph.co.uk/news/ribble_valley/langho/rss/",
    "https://www.lancashiretelegraph.co.uk/news/ribble_valley/longridge/rss/",
    "https://www.lancashiretelegraph.co.uk/news/ribble_valley/mellor/rss/",
    "https://www.lancashiretelegraph.co.uk/news/ribble_valley/ribchester/rss/",
    "https://www.lancashiretelegraph.co.uk/news/ribble_valley/sabden/rss/",
    "https://www.lancashiretelegraph.co.uk/news/ribble_valley/simonstone/rss/",
    "https://www.lancashiretelegraph.co.uk/news/ribble_valley/whalley/rss/",
    "https://www.lancashiretelegraph.co.uk/news/hyndburn/rss/",
    "https://www.lancashiretelegraph.co.uk/news/hyndburn/accrington/rss/",
    "https://www.lancashiretelegraph.co.uk/news/hyndburn/baxenden/rss/",
    "https://www.lancashiretelegraph.co.uk/news/hyndburn/church/rss/",
    "https://www.lancashiretelegraph.co.uk/news/hyndburn/clayton_le_moors/rss/",
    "https://www.lancashiretelegraph.co.uk/news/hyndburn/huncoat/rss/",
    "https://www.lancashiretelegraph.co.uk/news/hyndburn/knuzden/rss/",
    "https://www.lancashiretelegraph.co.uk/news/hyndburn/oswaldtwistle/rss/",
    "https://www.lancashiretelegraph.co.uk/news/hyndburn/rishton/rss/",
    "https://www.lancashiretelegraph.co.uk/news/rossendale/rss/",
    "https://www.lancashiretelegraph.co.uk/news/rossendale/bacup/rss/",
    "https://www.lancashiretelegraph.co.uk/news/rossendale/edenfield/rss/",
    "https://www.lancashiretelegraph.co.uk/news/rossendale/haslingden/rss/",
    "https://www.lancashiretelegraph.co.uk/news/rossendale/ramsbottom/rss/",
    "https://www.lancashiretelegraph.co.uk/news/rossendale/rawtenstall/rss/",
    "https://www.lancashiretelegraph.co.uk/news/rossendale/stacksteads/rss/",
    "https://www.lancashiretelegraph.co.uk/news/rossendale/waterfoot/rss/",
    "https://www.lancashiretelegraph.co.uk/news/rossendale/whitworth/rss/",
    "https://www.lancashiretelegraph.co.uk/news/pendle/rss/",
    "https://www.lancashiretelegraph.co.uk/news/pendle/barnoldswick/rss/",
    "https://www.lancashiretelegraph.co.uk/news/pendle/barrowford/rss/",
    "https://www.lancashiretelegraph.co.uk/news/pendle/blacko/rss/",
    "https://www.lancashiretelegraph.co.uk/news/pendle/brierfield/rss/",
    "https://www.lancashiretelegraph.co.uk/news/pendle/colne/rss/",
    "https://www.lancashiretelegraph.co.uk/news/pendle/earby/rss/",
    "https://www.lancashiretelegraph.co.uk/news/pendle/fence/rss/",
    "https://www.lancashiretelegraph.co.uk/news/pendle/foulridge/rss/",
    "https://www.lancashiretelegraph.co.uk/news/pendle/kelbrook/rss/",
    "https://www.lancashiretelegraph.co.uk/news/pendle/nelson/rss/",
    "https://www.lancashiretelegraph.co.uk/news/pendle/nelson/rss/",
    "https://www.lancashiretelegraph.co.uk/news/pendle/nelson/rss/",
    "https://www.lancashiretelegraph.co.uk/news/pendle/reedley/rss/",
    "https://www.lancashiretelegraph.co.uk/news/business/rss/",
    "https://www.lancashiretelegraph.co.uk/news/coronavirus/rss/",
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
    
async def scan():
    return False
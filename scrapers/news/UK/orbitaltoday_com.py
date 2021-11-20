Q ='Q107971243'
urls = [
    "https://orbitaltoday.com/"
]
feeds = [
"https://orbitaltoday.com/category/news/feed",
"https://orbitaltoday.com/category/features/feed",
"https://orbitaltoday.com/category/news/uk-space-industry/feed",
"https://orbitaltoday.com/category/news/environment/feed",
"https://orbitaltoday.com/category/news/earth-observation/feed",
"https://orbitaltoday.com/category/features/people-in-space/feed",
"https://orbitaltoday.com/tag/aac-clyde-space/feed",
"https://orbitaltoday.com/tag/alba-orbital/feed",
"https://orbitaltoday.com/tag/boeing/feed",
"https://orbitaltoday.com/tag/chris-larmour/feed",
"https://orbitaltoday.com/tag/craig-clark/feed",
"https://orbitaltoday.com/tag/electron-rocket/feed",
"https://orbitaltoday.com/tag/firefly-aerospace/feed",
"https://orbitaltoday.com/tag/highlands-islands-enterprise/feed",
"https://orbitaltoday.com/tag/kristian-von-bengtson/feed",
"https://orbitaltoday.com/tag/laura-edison/feed",
"https://orbitaltoday.com/tag/iss/feed",
"https://orbitaltoday.com/tag/moonspike/feed",
"https://orbitaltoday.com/tag/ohb-space/feed",
"https://orbitaltoday.com/tag/peter-guthrie/feed",
"https://orbitaltoday.com/tag/prestwick-spaceport/feed",
"https://orbitaltoday.com/tag/rocket-explosion/feed",
"https://orbitaltoday.com/tag/launch/feed",
"https://orbitaltoday.com/tag/scottish-spaceport/feed",
"https://orbitaltoday.com/tag/skyrora/feed",
"https://orbitaltoday.com/tag/space-careers/feed",
"https://orbitaltoday.com/tag/spacetechexpo/feed",
"https://orbitaltoday.com/tag/spaceport-cornwall/feed",
"https://orbitaltoday.com/tag/starliner/feed",
"https://orbitaltoday.com/tag/uk-rockets/feed",
"https://orbitaltoday.com/tag/uk-space-race/feed",
"https://orbitaltoday.com/tag/vertical-launch/feed",
"https://orbitaltoday.com/tag/volodymyr-levykin/feed",
"https://orbitaltoday.com/tag/abl-space/feed",
"https://orbitaltoday.com/tag/black-arrow/feed",
"https://orbitaltoday.com/tag/brexit/feed",
"https://orbitaltoday.com/tag/climate-change/feed",
"https://orbitaltoday.com/tag/ecometrica/feed",
"https://orbitaltoday.com/tag/european-space-agency/feed",
"https://orbitaltoday.com/tag/gilmour-space-technologies/feed",
"https://orbitaltoday.com/tag/horizontal-launch/feed",
"https://orbitaltoday.com/tag/jeff-bezos/feed",
"https://orbitaltoday.com/tag/llandebr/feed",
"https://orbitaltoday.com/tag/mars/feed",
"https://orbitaltoday.com/tag/nasa/feed",
"https://orbitaltoday.com/tag/oneweb/feed",
"https://orbitaltoday.com/tag/peter-madsen/feed",
"https://orbitaltoday.com/tag/proton-rocket/feed",
"https://orbitaltoday.com/tag/rocket-factory-augsburg/feed",
"https://orbitaltoday.com/tag/satellites/feed",
"https://orbitaltoday.com/tag/shetland-space-centre/feed",
"https://orbitaltoday.com/tag/snowdonia-spaceport/feed",
"https://orbitaltoday.com/tag/space-debris/feed",
"https://orbitaltoday.com/tag/space-tourism/feed",
"https://orbitaltoday.com/tag/starlink/feed",
"https://orbitaltoday.com/tag/uk-space-agency/feed",
"https://orbitaltoday.com/tag/spacex/feed",
"https://orbitaltoday.com/tag/uk-spaceport/feed",
"https://orbitaltoday.com/tag/virgin-galactic/feed",
"https://orbitaltoday.com/tag/alaska-space/feed",
"https://orbitaltoday.com/tag/catriona-francis/feed",
"https://orbitaltoday.com/tag/copenhagen-suborbitals/feed",
"https://orbitaltoday.com/tag/elecnor-deimos/feed",
"https://orbitaltoday.com/tag/falcon-9/feed",
"https://orbitaltoday.com/tag/goonhilly/feed",
"https://orbitaltoday.com/tag/isar-aerospace/feed",
"https://orbitaltoday.com/tag/kodiak-launch/feed",
"https://orbitaltoday.com/tag/lockheed-martin/feed",
"https://orbitaltoday.com/tag/moon/feed",
"https://orbitaltoday.com/tag/new-shepard/feed",
"https://orbitaltoday.com/tag/orbex-space/feed",
"https://orbitaltoday.com/tag/pld-space/feed",
"https://orbitaltoday.com/tag/richard-branson/feed",
"https://orbitaltoday.com/tag/rocket-lab/feed",
"https://orbitaltoday.com/tag/scotland/feed",
"https://orbitaltoday.com/tag/skylark-nano/feed",
"https://orbitaltoday.com/tag/space-apprenticeship/feed",
"https://orbitaltoday.com/tag/space-scholarship/feed",
"https://orbitaltoday.com/tag/spaceport/feed",
"https://orbitaltoday.com/tag/spire/feed",
"https://orbitaltoday.com/tag/sutherland-spaceport/feed",
"https://orbitaltoday.com/tag/uk-space-conference/feed",
"https://orbitaltoday.com/tag/vector-launch/feed",
"https://orbitaltoday.com/tag/virgin-orbit/feed",
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
    headline =  soup.select('h1.chapter-ttl')[0]
    for s in soup.select('.article-chapter > :not(p,h2)'):
        s.extract()
    for s in soup.select('img'):
        s.extract()
    for s in soup.select('script'):
        s.extract()
    bodyCopy =  soup.select('.article-chapter')[0] ### READ THE FULL STORY
    
async def scan():
    return False

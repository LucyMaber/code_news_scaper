Q ='[[wikidata:Q7569853]]'
urls = [
    "https://www.dailyecho.co.uk/"
]
feeds = [
"https://www.dailyecho.co.uk/news/rss/",
"https://www.dailyecho.co.uk/news/district/rss/",
"https://www.dailyecho.co.uk/news/district/southampton/rss/",
"https://www.dailyecho.co.uk/news/district/eastleigh/rss/",
"https://www.dailyecho.co.uk/news/district/fareham_and_gosport/rss/",
"https://www.dailyecho.co.uk/news/district/newforest/rss/",
"https://www.dailyecho.co.uk/news/district/romsey/rss/",
"https://www.dailyecho.co.uk/news/district/winchester/rss/",
"https://www.dailyecho.co.uk/news/crime/rss/",
"https://www.dailyecho.co.uk/news/crime/lucy-mchugh/rss/",
"https://www.dailyecho.co.uk/news/education/rss/",
"https://www.dailyecho.co.uk/news/education/ofsted/rss/",
"https://www.dailyecho.co.uk/news/education/education_awards/rss/",
"https://www.dailyecho.co.uk/news/nightlife/rss/",
"https://www.dailyecho.co.uk/news/politics/rss/",
"https://www.dailyecho.co.uk/news/health/rss/",
"https://www.dailyecho.co.uk/news/general-election/rss/",
"https://www.dailyecho.co.uk/news/coronavirus/rss/",
"https://www.dailyecho.co.uk/yoursay/letters/rss/",
"https://www.dailyecho.co.uk/yoursay/blogs/ian_murray/rss/",
"https://www.dailyecho.co.uk/yoursay/blogs/win_with_kids/rss/",
"https://www.dailyecho.co.uk/yoursay/blogs/martin_lewis/rss/",
"https://www.dailyecho.co.uk/yoursay/blogs/talking_shop/rss/",
"https://www.dailyecho.co.uk/yoursay/blogs/winchester_bloke/rss/",
"https://www.dailyecho.co.uk/news/district/winchester/rss/",
"https://www.dailyecho.co.uk/news/crime/rss/",
"https://www.dailyecho.co.uk/news/crime/lucy-mchugh/rss/",
"https://www.dailyecho.co.uk/news/education/rss/",
"https://www.dailyecho.co.uk/news/education/ofsted/rss/",
"https://www.dailyecho.co.uk/news/education/education_awards/rss/",
"https://www.dailyecho.co.uk/news/nightlife/rss/",
"https://www.dailyecho.co.uk/news/politics/rss/",
"https://www.dailyecho.co.uk/news/general-election/rss/",
"https://www.dailyecho.co.uk/news/coronavirus/rss/",
"https://www.dailyecho.co.uk/yoursay/letters/rss/",
"https://www.dailyecho.co.uk/yoursay/blogs/tomkongwatson/rss/",
"https://www.dailyecho.co.uk/yoursay/letters/rss/",
"https://www.dailyecho.co.uk/yoursay/blogs/tomkongwatson/rss/",
"https://www.dailyecho.co.uk/yoursay/blogs/win_with_kids/rss/",
"https://www.dailyecho.co.uk/yoursay/blogs/martin_lewis/rss/",
"https://www.dailyecho.co.uk/yoursay/blogs/talking_shop/rss/",
"https://www.dailyecho.co.uk/yoursay/blogs/winchester_bloke/rss/",
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
    
async def scan():
    return False
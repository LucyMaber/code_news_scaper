urls = [
    "https://www.dailynews.com/"
]
feeds = [
    "https://www.dailynews.com/feed/"
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
    headline =  soup.select('h1.entry-title')[0]
    description =  soup.select('h2.subheadline')[0]
    author_name =  soup.select('.author-name')[0]
    time =  soup.select('time')[0]
    #dateModified =  soup.select('[itemprop="dateModified"]')[0]
    #publishedDate =  soup.select('.date-published')[0]
    for s in soup.select('.body-copy > :not(p , .twitter-tweet )'):
        s.extract()
    bodyCopy =  soup.select('.body-copy')[0]
    print(time)
article("https://www.dailynews.com/2021/11/03/la-mayor-eric-garcetti-test-positive-for-covid-19-during-scotland-trip/")
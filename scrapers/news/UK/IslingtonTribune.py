urls = []
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
    headline =  soup.select('.Article__main > div > div > div > h1')[0]
    tags =soup.select('.ArticleCategories__category')[0]
    # for s in soup.select('.Article__content  > div > :not(p, h1,h2,h3,h4,h5,h6) '):
    #     s.extract()
    article =  soup.select('.Article__content > div')[0]
    print(tags)
article("http://islingtontribune.com/article/care-homes-abuse-scandal-was-my-sons-life-worthless")

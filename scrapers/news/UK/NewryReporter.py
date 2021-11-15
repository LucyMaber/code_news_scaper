Q =""
urls = [
    "http://www.newryreporter.com/"
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
    headline =  soup.select('.section_content > h2')[0]
    time_by =  soup.select('.section_content > h3')[0]
    for s in soup.select('.section_content > :not(p)'):
        s.extract()
    for s in soup.select('.section_content > :contains("READ THE FULL STORY")'):
        s.extract()
    bodyCopy =  soup.select('.section_content')[0] ### READ THE FULL STORY
    
article("http://www.newryreporter.com/pages/?title=40m-health-hub-to-open-in-2025")

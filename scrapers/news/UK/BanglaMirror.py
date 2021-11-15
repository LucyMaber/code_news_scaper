Q ='[[wikidata:Q4855248]]'
urls = [
    "https://banglamirrornews.com/"
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
    # Need to add author
    headline =  soup.select('[itemprop="name"]') [0]
    for s in soup.select(".addtoany_share_save_container addtoany_content addtoany_content_bottom"):
        s.extract()
    for s in soup.select(".addtoany_share_save_container addtoany_content addtoany_content_top"):
        s.extract()
    for s in soup.select("img"):
        s.extract()
    article_body =  soup.select('div.entry') [0]
    
article("https://banglamirrornews.com/2021/11/01/we-are-digging-our-own-graves/")
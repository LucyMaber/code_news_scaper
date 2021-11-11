urls = [
    "https://www.thejc.com/"
]
feeds = [
    "https://www.thejc.com/cmlink/rss-jewish-chronicle-us-news-1.485395",
    "https://www.thejc.com/cmlink/rss-jewish-chronicle-uk-news-1.485394",
    "https://www.thejc.com/cmlink/rss-jewish-chronicle-world-news-1.485393",
    "https://www.thejc.com/cmlink/rss-jewish-chronicle-news-1.438559",
    "https://www.thejc.com/cmlink/rss-jewish-chronicle-community-1.484984",
    "https://www.thejc.com/cmlink/rss-jewish-chronicle-culture-1.484988",
    "https://www.thejc.com/cmlink/rss-jewish-chronicle-education-1.485386",
    "https://www.thejc.com/cmlink/rss-jewish-chronicle-travel-1.485387",
    "https://www.thejc.com/cmlink/rss-jewish-chronicle-food-1.485388",
    "https://www.thejc.com/cmlink/rss-jewish-chronicle-interviews-1.485389",
    "https://www.thejc.com/cmlink/rss-jewish-chronicle-interviews-1.485389",
    "https://www.thejc.com/cmlink/rss-jewish-chronicle-comment-1.485390",
    "https://www.thejc.com/cmlink/rss-jewish-chronicle-mgbsfl-1.485391",
    "https://www.thejc.com/cmlink/rss-jewish-chronicle-israel-news-1.485392",
]
header={
    # 'sec-ch-ua': 'Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': 'Linux',
    # 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
}


from bs4 import BeautifulSoup
import requests

def article(url):
    req = requests.get(url,headers=header)
    content = req.content
    soup = BeautifulSoup(content, 'html.parser')
    headline =  soup.select('[class="article-heading__content"]')[0]
    subheadline =  soup.select('.standfirst')[0]
    for s in soup.select('script'):
        s.extract()
    for s in soup.select('.article section > :contains("For the latest Hull crime news straight into your inbox,")'):
        s.extract()
    content =  soup.select('.article > .prose')[0]
    print(content)
article("https://www.thejc.com/comment/opinion/diversity-obsession-has-ruined-the-marvel-fun-1.522406")

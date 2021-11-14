urls = [
    "https://www.gazetteandherald.co.uk/"
]
feeds = [
    "https://www.gazetteandherald.co.uk/news/rss/",
    "https://www.gazetteandherald.co.uk/news/headlines/nostalgia/rss/",
    "https://www.gazetteandherald.co.uk/news/headlines/weddings/rss/",
    "https://www.gazetteandherald.co.uk/news/towns/calneheadlines/rss/",
    "https://www.gazetteandherald.co.uk/news/towns/chippenhamheadlines/rss/",
    "https://www.gazetteandherald.co.uk/news/towns/corshamheadlines/rss/",
    "https://www.gazetteandherald.co.uk/news/towns/malmesburyheadlines/rss/",
    "https://www.gazetteandherald.co.uk/news/towns/marlboroughheadlines/rss/",
    "https://www.gazetteandherald.co.uk/news/towns/pewseynews/rss/",
    "https://www.gazetteandherald.co.uk/news/towns/woottonbassett/rss/",
    "https://www.gazetteandherald.co.uk/news/towns/pewseynews/rss/",
    "https://www.gazetteandherald.co.uk/news/towns/wiltshire/rss/",
    "https://www.gazetteandherald.co.uk/news/coronavirus/rss/",
    "https://www.gazetteandherald.co.uk/news/gazette_and_herald_columnists/rss/",
    "https://www.gazetteandherald.co.uk/news/national/rss/",
    "https://www.gazetteandherald.co.uk/news/national/uk-today/rss/"
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
    for s in soup.select('.subscription-content > :not(p)'):
        s.extract()
    content =  soup.select('.subscription-content')[0]
    
article("https://www.gazetteandherald.co.uk/news/19690841.public-notices-restaurants-pubs-road-closures/")
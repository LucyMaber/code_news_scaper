
from bs4 import BeautifulSoup
import validators


def readFeedHTML(content):
    isGood = False
    list_pace = []
    try:
        soup = BeautifulSoup(content, 'html.parser')
        # hAtom
        for hfeed in (soup.select('[rel="hfeed"],.hfeed')):
            for hentry in hfeed.select('[rel="hentry"],.hentry'):
                for bookmark in hentry.select('[rel="bookmark"], .bookmark'):
                    if bookmark.has_attr("href") and validators.url(bookmark['href']):
                        link = {"where": bookmark["href"]}
                        list_pace.append(link)
        # hslice
        for hslice in (soup.select('[rel="hslice"],.hslice')):
            for bookmark in hslice.select('[rel="bookmark"], .bookmark'):
                    if bookmark.has_attr("href") and validators.url(bookmark['href']):
                        link = {"where": bookmark["href"]}
                        list_pace.append(link)
        return isGood,  list_pace
    except:
        return False, list_pace


def readFeedRSS(content):
    isGood = False
    list_pace = []
    try:
        soup = BeautifulSoup(content, 'lxml')
        for rss in soup.select('rss'):
            for channel in rss.select('channel'):
                for item in channel.select('item'):
                    for i in item.select('link'):
                        description = item.select('description')[0]
                        where = item.select('link')[0]
                        title = item.select('title')[0]
                        link = {"title": title, "where": where, "description": description}
                        list_pace.append(link)
        return isGood, list_pace
    except:
        return False, list_pace


def readFeedAtom(content):
    list_pace = []
    isGood = False
    try:
        soup = BeautifulSoup(content, 'lxml')
        for feed in soup.select('feed'):
            for entry in feed.select('entry'):
                for i in feed.select('link'):
                    title = entry.select('title') [0]
                    description = entry.select('summary') [0]
                    link = {"title": title, "where": i, "description": description}
                    list_pace.append(link)
        return isGood,  list_pace
    except:
        return False, list_pace


def readFeedJSON(content):
    isGood = False
    list_pace = []
    try:
        for item in content["items"]:
            if (validators.url(str(item["url"]))):
                link = {"count": item["content_text"], "where": item["url"]}
                isGood = True
                try:
                    link["href"] = item["url"]
                    list_pace.append(link)
                except:
                    pass
        return isGood,  list_pace
    except:
        return False, list_pace

from bs4 import BeautifulSoup
import requests
import validators
import json

FeedTypes = []
places = []
feed_list = []

FeedRssTypes = [
    'application/rss+xml',
    'application/rss',
    'text/rss+xml',
    'text/rss',
]
feedJsonTypes = [
    'application/feed+json',
    'text/feed+json',
]
HTMLTypes = [
    "application/x-hatom",
    "application/xhtml+xml",
    "application/html",
    "text/html",
    "html",
    "text/html; charset=utf-8"
]
FeedTypes = FeedRssTypes+feedJsonTypes+HTMLTypes

def scanHTML(content, place):
        isGood = False
        isFeed = False
        soup = BeautifulSoup(content, 'html.parser')
        # # hAtom
        # for hfeed in (soup.select('[rel="hfeed"],.hfeed')):
        #     for hentry in hfeed.select('[rel="hentry"],.hentry'):
        #         for bookmark in hentry.select('[rel="bookmark"], .bookmark'):
        #             if bookmark.has_attr("href") and validators.url(bookmark['href']):
        #                 link = {"count": place["count"],
        #                         "where": bookmark["href"]}
        #                 places.append(link)
        #                 isFeed = True
        # # hslice
        # for hslice in (soup.select('[rel="hslice"],.hslice')):
        #     for bookmark in hslice.select('[rel="bookmark"], .bookmark'):
        #         if bookmark.has_attr("href") and validators.url(bookmark['href']):
        #             link = {"count": place["count"], "where": bookmark["href"]}
        #             feed_list.append(link)
        #             isFeed = True
        # Scan for LINKS
        for i in (soup.select('area ,link ,a')):
                link = {"count": place["count"], "href": i["href"], "where": i["href"]}
                if i.has_attr('rel'):
                    if "stylesheet" in i["rel"]:
                        continue
                    if "modulepreload" in i["rel"]:
                        continue
                    if "manifest" in i["rel"]:
                        continue
                    if "license" in i["rel"]:
                        continue
                    if "noreferrer" in i["rel"]:
                        continue
                    if "help" in i["rel"]:
                        continue
                    if "icon" in i["rel"]:
                        continue
                    if "canonical" in i["rel"]:
                        continue
                    if "author" in i["rel"]:
                        continue
                    if "dns-prefetch" in i["rel"]:
                        continue
                    link["rel"] = i["rel"]
                if i.has_attr('type'):
                    link["type"] = i["type"]
                    if i["type"] in FeedTypes:
                        feed_list.append(link)
                    else:
                        continue
                places.append(link)
        if isFeed:
            place["type"] = "HTML_Feed"
            feed_list.append(place)
        return isGood

headers = {

}
# headers["Content-Type"] = "application/xml"
content = requests.get('https://www.bbc.co.uk/', headers=headers).text
place = {"count": 4, "where": "https://www.bbc.co.uk/"}
# print(content)
scanHTML(content, place)
print(places)
from bs4 import BeautifulSoup

from reqest_man import reqest_saferobot
from uitls.enlightenPlus.cache import cache
urls = [
    "http://biglistofwebsites.com/lists/A",
    "http://biglistofwebsites.com/lists/B",
    "http://biglistofwebsites.com/lists/C",
    "http://biglistofwebsites.com/lists/D",
    "http://biglistofwebsites.com/lists/E",
    "http://biglistofwebsites.com/lists/F",
    "http://biglistofwebsites.com/lists/G",
    "http://biglistofwebsites.com/lists/H",
    "http://biglistofwebsites.com/lists/I",
    "http://biglistofwebsites.com/lists/J",
    "http://biglistofwebsites.com/lists/K",
    "http://biglistofwebsites.com/lists/L",
    "http://biglistofwebsites.com/lists/M",
    "http://biglistofwebsites.com/lists/M",
    "http://biglistofwebsites.com/lists/O",
    "http://biglistofwebsites.com/lists/P",
    "http://biglistofwebsites.com/lists/Q",
    "http://biglistofwebsites.com/lists/R",
    "http://biglistofwebsites.com/lists/S",
    "http://biglistofwebsites.com/lists/T",
    "http://biglistofwebsites.com/lists/X",
    "http://biglistofwebsites.com/lists/Y",
    "http://biglistofwebsites.com/lists/Z",
    "http://biglistofwebsites.com/list-top-websites-on-news",
    "http://biglistofwebsites.com/list-top-websites-on-financial",
    "http://biglistofwebsites.com/list-top-websites-on-server",
    "http://biglistofwebsites.com/list-top-websites-on-politics",
    "http://biglistofwebsites.com/list-top-websites-on-tech",
    "http://biglistofwebsites.com/list-top-websites-on-computers",
    "http://biglistofwebsites.com/list-top-websites-on-music",
    "http://biglistofwebsites.com/list-top-websites-on-xbox",
    "http://biglistofwebsites.com/list-top-websites-on-sport",
    "http://biglistofwebsites.com/list-top-websites-on-esport",
    "http://biglistofwebsites.com/list-top-websites-on-shopping",
    "http://biglistofwebsites.com/list-top-websites-on-cricket",
    "http://biglistofwebsites.com/list-top-websites-on-football",
    "http://biglistofwebsites.com/list-top-websites-on-tennis",
    "http://biglistofwebsites.com/list-top-websites-on-concert",
    "http://biglistofwebsites.com/list-top-websites-on-college",
    "http://biglistofwebsites.com/list-top-websites-on-Entertainment",
    "http://biglistofwebsites.com/list-top-websites-on-Gaming",
    "http://biglistofwebsites.com/list-top-websites-like-newegg.com",
    "http://biglistofwebsites.com/list-top-websites-like-cnet.com",
    "http://biglistofwebsites.com/list-top-websites-like-nytimes.com",
    "http://biglistofwebsites.com/list-top-websites-like-eharmony.com",
    "http://biglistofwebsites.com/list-top-websites-like-glassdoor.com",
    "http://biglistofwebsites.com/list-top-websites-like-dell.com",
    "http://biglistofwebsites.com/list-top-websites-like-dafont.com",
]
def crawling_big_list_of_websites ():
    href = []
    for url in urls:
        request = reqest_saferobot(url)
        soup = BeautifulSoup(request.text, 'html.parser')
        for a in soup.select(".cell-row.hover-highlight .cell .cell.cell-md  a"):
            href.append((a["href"]))
    cache.set("crawling_big_list_of_websites",href)
    return href
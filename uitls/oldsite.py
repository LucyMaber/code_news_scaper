import json
from logging import log
from os import EX_OSFILE
from time import sleep
from bs4 import BeautifulSoup
import waybackpy
import requests
from urllib.parse import urljoin, urlparse
import markdownify
import shutil
import datetime
import re
import os

reg = r"(https:\/\/web\.archive\.org\/web\/[^/]*\/|\/web\/[^/]*\/)(.*)"


def getURL(url):
    sleep(4)
    response = requests.get(url, timeout=(3.05, 27))
    return response


def getURLSite(url):
    user_agent = ""
    wayback = waybackpy.Url(url, user_agent)
    if wayback.archive_url is None:
        return None
    print(wayback)
    response = getURL(wayback)
    return response


urls = []

walk_page = []


def page_walker(url):
    pages = {}
    try:
        response = getURL(url)
    except:
        return pages
    if response.status_code == 404:
        m = re.search(reg, url)
        response = getURLSite(m.group(2))
        if response is None:
            return pages
        if response.status_code == 404:
            return pages
    if url in walk_page:
        return[]
    walk_page.append(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    for content in soup.select("#content-primary .content"):
        post_title = content.select("a")[0]
        summery = content.select(".views-field-body")
        name = content.select(".views-field-title")
        if len(summery) >= 1:
            summery = summery[0].prettify()
        else:
            summery = ""
        if len(name) >= 1:
            name = name[0].get_text()
        else:
            name = ""
        ur = urljoin(url, post_title['href'])
        m = re.search(reg, ur)
        ur_test = urlparse(m.group(2)).path
        if ur_test in urls:
            continue
        data, t = passAcartal(ur, summery, name)
        if t:
            pages[urlparse(m.group(2)).path] = data
        else:
            if m.group(2) not in pages.keys():
                pages[urlparse(m.group(2)).path] = data

    for pager in soup.select(".pager a"):
        ur = urljoin(url, pager['href'])
        if ur in urls:
            continue
        urls.append(ur)
        p = page_walker(ur)
        for px in p.keys():
            pages[px] = p[px]
    return pages


def passAcartal(url, summery, name):
    m = re.search(reg, url)
    doc = {
        "state": "summery_only",
        "summery": summery,
        "url": m.group(2),
        "where": url,
        "title": name,
    }
    m = re.search(reg, url)
    ur_test = urlparse(m.group(2)).path
    m = re.search(reg, url)
    print("found artical at:", url)
    response = getURL(url)
    if response.status_code == 404:
        response = getURLSite(m.group(2))
        if response is None:
            print("return: ", 0)
            return doc, False
        if response.status_code == 404:
            print("return: ", 1)
            print(doc)
            return doc, False
    else:
        urls.append(ur_test)
    soup = BeautifulSoup(response.content, 'html.parser')
    for content in soup.select("#content-primary"):
        f_doc = {
            "state": "full",
            "title": "",
            "body": "",
            "summery": markdownify.markdownify(summery, heading_style="ATX"),
            "tags": [],
            "source": [],
            "url": m.group(2),
            "where": url
        }

        links = content.select("a")
        for i in links:
            try:
                ms = re.search(reg,  i["href"])
                if  ".pirateparty.org.uk" in i["href"]:
                    i["href"] =  urlparse(ms.group(2)).path
                else:
                    i["href"] = ms.group(2)
            except:
                pass

        links = content.select("img")
        for i in links:
            try:
                p = urlparse(ms.group(2)).path
                filePath = os.path.join("./oldsite",p)
                ms = re.search(reg,  i["href"])
                if  ".pirateparty.org.uk" in i["href"]:
                    response = getURL(url)
                    if response.status_code == 404:
                        response = getURLSite(ms.group(2))
                        if response.status_code == 404 or response is None:
                            pass
                        else:
                            with open(filePath, 'wb') as out_file:
                                shutil.copyfileobj(response.raw, out_file)
                            del response
                    else:
                        with open(filePath, 'wb') as out_file:
                            shutil.copyfileobj(response.raw, out_file)
                        del response
                    i["href"] =  urlparse(ms.group(2)).path
                else:
                    i["href"] = ms.group(2)
            except:
                pass
        title = content.select(".page-title,.page-title,h1")
        if len(title) > 0:
            f_doc["title"] = title[0].get_text().replace("\n", "")
        body = content.select(".field-name-body")
        if len(body) > 0:
            f_doc["body"] = markdownify.markdownify(
                body[0].prettify(), heading_style="ATX")
        tags = content.select(".field-name-field-tags > .field-items  a")
        for tag in tags:
            f_doc["tags"].append(tag.get_text())
        sources = content.select(".field-name-field-source-link a")
        for source in sources:
            f_doc["source"].append(source["href"])
        date = content.select(
            ".field-name-field-date-of-report span,.submitted span")
        if len(date) > 0:
            try:
                f_doc["date"] = date[0]["content"]
            except:
                pass
        date = content.select(".submitted span")
        if len(date) > 0:
            try:
                f_doc["date"] = date[0]["content"]
            except:
                pass
        contact_name = content.select(".field-name-field-contact-name")
        if len(contact_name) > 0:
            f_doc["name"] = contact_name[0].get_text().replace("\n", "")
        email = content.select(".field-name-field-contact-email a")
        if len(email) > 0:
            try:
                f_doc["email"] = email[0].get_text()
            except:
                pass
        dateline = content.select(".field-name-field-dateline span")
        print(len(dateline))
        if len(dateline) > 0:
            f_doc["date"] = dateline[0]["content"]
        dateline = content.select(".field-name-field-release-date span")
        print(len(dateline))
        if len(dateline) > 0:
            f_doc["date"] = dateline[0]["content"]
        print(f_doc)
        print("return: ", 2)
        return f_doc, True
    return doc, True


docs_output = {}
f = [
    "https://web.archive.org/web/20190414152001/https://www.pirateparty.org.uk/",
    "https://web.archive.org/web/20190414152001/https://www.pirateparty.org.uk/blog",
    "https://web.archive.org/web/20190414152001/https://www.pirateparty.org.uk/party/press-hits",
    "https://web.archive.org/web/20190414152001/https://www.pirateparty.org.uk/press-release",
    "https://web.archive.org/web/20201029132944/https://legacy.pirateparty.org.uk/",
    "https://web.archive.org/web/20201029140955/https://legacy.pirateparty.org.uk/party/press-hits",
    "https://web.archive.org/web/20201022204013/https://legacy.pirateparty.org.uk/press-release",
    "https://web.archive.org/web/20190414153153/https://www.legacy.pirateparty.org.uk/blog",
    "https://web.archive.org/web/20170609224310/https://www.pirateparty.org.uk/press-release"
]
for i in f:
    p = page_walker(i)
    for x in p.keys():
        if p[x]["state"] == "full":
            docs_output[x] = p[x]
        else:
            if x not in docs_output.keys():
                docs_output[x] = p[x]

jso = json.dumps(docs_output)

f = open("legacy_pirateparty.json", "w")
f.write(jso)
f.close()


def recoder(content, doc={}):
    summery = content.select(".views-field-body")
    if len(summery) >= 1:
        doc["summery"] = summery[0].prettify()
    name = content.select(".views-field-title")
    if len(name) >= 1:
        doc["name"] = name[0].get_text()
    title = content.select(".page-title,.page-title,h1")
    if len(title) > 0:
        doc["title"] = title[0].get_text().replace("\n", "")
    body = content.select(".field-name-body")
    if len(body) > 0:
        doc["body"] = markdownify.markdownify(
            body[0].prettify(), heading_style="ATX")
    tags = content.select(".field-name-field-tags > .field-items  a")
    for tag in tags:
        doc["tags"].append(tag.get_text())
    sources = content.select(".field-name-field-source-link a")
    for source in sources:
        doc["source"].append(source["href"])
    date = content.select(
        ".field-name-field-date-of-report span,.submitted span")
    if len(date) > 0:
        try:
            doc["date"] = date[0]["content"]
        except:
            pass
    date = content.select(".submitted span")
    if len(date) > 0:
        try:
            doc["date"] = date[0]["content"]
        except:
            pass
    contact_name = content.select(".field-name-field-contact-name")
    if len(contact_name) > 0:
        doc["name"] = contact_name[0].get_text().replace("\n", "")
    email = content.select(".field-name-field-contact-email a")
    if len(email) > 0:
        try:
            doc["email"] = email[0].get_text()
        except:
            pass
    dateline = content.select(".field-name-field-dateline span")
    if len(dateline) > 0:
        doc["date"] = dateline[0]["content"]
    dateline = content.select(".field-name-field-release-date span")
    if len(dateline) > 0:
        doc["date"] = dateline[0]["content"]
    return doc

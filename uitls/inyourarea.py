from asyncio.tasks import sleep
import asyncio
from pyppeteer import launch
import csv


def postcode_generator():
    with open('ukpostcodes.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            yield(row['postcode'].replace(" ", ""))


async def feed(post, where, page, browser):
    while (True):
        try:
            await page.goto('https://www.inyourarea.co.uk/feed/'+post+"/"+where+"/news/all", {'waitUntil': ['networkidle0', "load", "domcontentloaded"]})
            elements = await page.querySelectorAllEval('a[class*="style_titleLink"]', """(e) => {
                                out = []
                                for (const element of e) {
                                    out.push(element.getAttribute("href"));  
                                    }
                                    return out;
                                }""")
            return where, page, browser ,elements
        except:
            await page.close()
            page = await browser.newPage()


async def notices(post, page, browser):
    while (True):
        try:
            await page.goto('https://www.inyourarea.co.uk/notices/'+post+"/all", {'waitUntil': ['networkidle0', "load", "domcontentloaded"]})
            elements = await page.querySelectorAllEval('[class*="style_featuredWrapper"]>div>div>div>div>a', """(e) => {
            out = []
            for (const element of e) {
                out.push(element.getAttribute("href"));  
                }
                return out;
            }""")
            return page, browser ,elements
        except:
            await page.close()
            page = await browser.newPage()


async def mynews(post, where, page, browser):
    while (True):
        try:
            await page.goto('https://www.inyourarea.co.uk/feed/'+post+"/"+where+"/news/mynews", {'waitUntil': ['networkidle0', "load", "domcontentloaded"]})
            elements = await page.querySelectorAllEval('a[class*="style_titleLink"]', """(e) => {
                                out = []
                                for (const element of e) {
                                    out.push(element.getAttribute("href"));  
                                    }
                                    return out;
                                }""")
            return where, page, browser ,elements
        except:
            await page.close()
            page = await browser.newPage()


async def feedFinder(post, page, browser):
    while True:
        try:
            await page.goto('https://www.inyourarea.co.uk/feed/'+post, {'waitUntil': ['networkidle0', "load", "domcontentloaded"]})
            elements = await page.querySelectorAllEval('.style_town_tY0jv > span', """(e) => {
                    out = []
                    for (const element of e) {
                        out.push(element.innerText);  
                        }
                        return out;
                    }""")
            for where in elements:
                test = True
            return post, page, browser ,elements
        except:
            await page.close()
            page = await browser.newPage()


async def scan_inyourarea():
    lookat = []
    for post in postcode_generator():
        browser = await launch({"headless": True, "args": ['--disable-gpu', '--no-sandbox', '--lang=en-US', '--disable-setuid-sandbox', '--disable-dev-shm-usage']})
        page = await browser.newPage()
        post, page, browser ,wheres = await feedFinder(post, page, browser)
        for where in wheres:
            where, page, browser ,feed_list = await feed(post, where, page, browser)
            lookat = lookat + feed_list
            page, browser ,notices_list = await notices(post, page, browser)
            lookat = lookat + notices_list
            where, page, browser ,mynews_list = await mynews(post, where, page, browser)
            lookat = lookat + mynews_list
    browser.close()
    return lookat

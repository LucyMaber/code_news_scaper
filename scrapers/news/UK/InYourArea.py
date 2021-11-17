import csv
from asyncio.tasks import sleep
from pyppeteer import launch
import asyncio
from bs4 import BeautifulSoup
import requests
Q =''
urls = [
    "https://www.inyourarea.co.uk/"
]
feeds = [
]

header={
    'sec-ch-ua': 'Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': 'Linux',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
}
def postcode_generator():
    with open('ukpostcodes.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            yield(row['postcode'])

def article(url):
    if "news" in url:
        content = requests.get(url,headers=header).content
        soup = BeautifulSoup(content, 'html.parser')
        headline =  soup.select('header > h1')[0]
        article =  soup.select('#post-content')[0]
    elif "notices" in url:
        content = requests.get(url,headers=header).content
        soup = BeautifulSoup(content, 'html.parser')
        headline =  soup.select('h1')[0]
        article =  soup.select('p')[0]
async def scan():
    return False

async def scan():
    for post in postcode_generator():
        browser = await launch({ "headless": True })
        page = await browser.newPage()
        while(True):
            try:
                await page.goto('https://www.inyourarea.co.uk/feed/'+post, {'waitUntil' : ['networkidle0',"load","domcontentloaded"]})
                elements = await page.querySelectorAllEval('.style_town_tY0jv > span',"""(e) => {
                out = []
                for (const element of e) {
                    out.push(element.innerText);  
                    }
                    return out;
                }""")
                for where in elements:
                    while (True):
                        try:
                                await page.goto('https://www.inyourarea.co.uk/feed/'+post+"/"+where+"/news/all", {'waitUntil' : ['networkidle0',"load","domcontentloaded"]})
                                elements = await page.querySelectorAllEval('a[class*="style_titleLink"]',"""(e) => {
                                out = []
                                for (const element of e) {
                                    out.push(element.getAttribute("href"));  
                                    }
                                    return out;
                                }""")
                                break
                        except:
                            browser = await launch({ "headless": True })
                            page = await browser.newPage()
                            await page.goto('https://www.inyourarea.co.uk/feed/'+post+"/"+where+"/news/all", {'waitUntil' : ['networkidle0',"load","domcontentloaded"]})
                
                for where in elements:
                    while (True):
                        try:
                                await page.goto('https://www.inyourarea.co.uk/feed/'+post+"/"+where+"/news/mynews", {'waitUntil' : ['networkidle0',"load","domcontentloaded"]})
                                elements = await page.querySelectorAllEval('a[class*="style_titleLink"]',"""(e) => {
                                out = []
                                for (const element of e) {
                                    out.push(element.getAttribute("href"));  
                                    }
                                    return out;
                                }""")
                                break
                        except:
                            browser = await launch({ "headless": True })
                            page = await browser.newPage()
                            await page.goto('https://www.inyourarea.co.uk/feed/'+post+"/"+where+"/news/mynews", {'waitUntil' : ['networkidle0',"load","domcontentloaded"]})
                
                while (True):
                    try:
                        await page.goto('https://www.inyourarea.co.uk/notices/'+post+"/all", {'waitUntil' : ['networkidle0',"load","domcontentloaded"]})
                        elements = await page.querySelectorAllEval('[class*="style_featuredWrapper"]>div>div>div>div>a',"""(e) => {
                        out = []
                        for (const element of e) {
                            out.push(element.getAttribute("href"));  
                            }
                            return out;
                        }""")
            
                        break
                    except:
                        await page.goto('https://www.inyourarea.co.uk/notices/'+post+"/all", {'waitUntil' : ['networkidle0',"load","domcontentloaded"]})
                await browser.close()
                print("count")
            except:
                await browser.close()
                browser = await launch({ "headless": True })
                page = await browser.newPage()
    return True

#asyncio.get_event_loop().run_until_complete(scan())


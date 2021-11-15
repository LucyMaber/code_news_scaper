import csv

def postcode_generator():
    with open('ukpostcodes.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['postcode'])
            yield(row['postcode'])
from asyncio.tasks import sleep
from pyppeteer import launch
import asyncio
async def main():
    for post in postcode_generator():
        browser = await launch({ "headless": False })
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
                print(elements)
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
                            browser = await launch({ "headless": False })
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
                                print(elements)
                                break
                        except:
                            browser = await launch({ "headless": False })
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
                        print(elements)
                        break
                    except:
                        await page.goto('https://www.inyourarea.co.uk/notices/'+post+"/all", {'waitUntil' : ['networkidle0',"load","domcontentloaded"]})
                await browser.close()
            except:
                await browser.close()
                browser = await launch({ "headless": False })
                page = await browser.newPage()

asyncio.get_event_loop().run_until_complete(main())


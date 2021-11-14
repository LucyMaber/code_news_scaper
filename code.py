import os
import importlib.util
import pywikibot

from os import listdir
from os.path import isfile, join
mypath = "/home/william/Code/news_scaper/scrapers/news/UK"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]


def path_import(absolute_path, file):
    spec = importlib.util.spec_from_file_location(file, absolute_path)
    # creating a new module based on spec
    foo = importlib.util.module_from_spec(spec)
    # exec_module :- An abstract method that executes the module in its own namespace when a module is imported or reloaded.
    spec.loader.exec_module(foo)
    return foo


output = open("demofile2.txt", "a")
urls = []
import re
for file in onlyfiles:
    name = re.sub(r"(\w)([A-Z])", r"\1 \2", file)
    try:
        name= name.replace('.py','')
        site = pywikibot.Site("en", "wikipedia")
        page = pywikibot.Page(site, name)
        item = str(pywikibot.ItemPage.fromPage(page))
    except:
        item = ""

    print(item)
    print(name)
    file = join(mypath, file)

    try:
        f = path_import(file,file)
        print(file)
        for i in f.urls:
            if i in urls:
                os.remove(file)
                continue
        
        with open(file, 'r') as original: 
            data = original.read()
            with open(file, 'w') as modified: 
                modified.write("Q ='" +item+"'\n"+ data)
                modified.close()
        if len(f.urls) == 0:
            output.write("Need URL:"+file + "\n") 
            continue
            urls.append(i)
        if len(f.feeds) == 0:
            output.write("Need Feed:"+file + "\n") 
    except:
        output.write("other Issue:"+file + "\n")
    

output.close()
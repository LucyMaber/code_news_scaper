import os
import importlib.util
from os import listdir
from os.path import isfile, join
mypath = "/home/william/Code/news_scaper/scrapers/news/UK"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for file in onlyfiles:
    file = join(mypath, file)
    f = open(file, "r")
    if "article" in f.read():
        os.remove(file)


from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import re

req = urlopen('https://www.10000recipe.com/recipe/list.html?q=&query=&cat1=&cat2=&cat3=&cat4=66&fct=&order=reco&lastcate=cat4&dsearch=&copyshot=&scrap=&degree=&portion=&time=&niresource=')

print(req.getcode())

if req.getcode() == 200:
    html = req.read()
    #print(html)

    html = html.decode("utf-8")
    #print(html)
else:
    print("HTTP ERROR")

soup = BeautifulSoup(html, "html.parser")
for i in range (1,20):
    rhead = soup.select('#contents_area_full > ul > ul > li:nth-child({}) > div.common_sp_caption > div.common_sp_caption_tit.line2'.format(i))
    for rheads in rhead:
        print(rheads.get_text())


#print(body ,body1 ,body2 , sep='\n')
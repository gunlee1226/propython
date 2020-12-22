from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import re

req = urlopen('https://www.10000recipe.com/recipe/6904344')

print(req.getcode())

if req.getcode() == 200:
    html = req.read()
    #print(html)

    html = html.decode("utf-8")
    #print(html)
else:
    print("HTTP ERROR")

soup = BeautifulSoup(html, "html.parser")

recipe_step = []
res = soup.select_one('div.view_step')
i = 0
for n in res.select('div.view_step_cont'):
    i = i + 1
    recipe_step.append('#' + str(i) + ' ' + n.get_text().replace('\n',' '))
print(recipe_step)
#print(body ,body1 ,body2 , sep='\n')
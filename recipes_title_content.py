from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

import dessertDAO as dao

req = urlopen('https://www.10000recipe.com/recipe/6846168')


print(req.getcode())

if req.getcode() == 200:
    html = req.read()
    #print(html)

    html = html.decode("utf-8")
    #print(html)
else:
    print("HTTP ERROR")

soup = BeautifulSoup(html, "html.parser")

r_title = soup.select_one('#contents_area > div.view2_summary.st3 > h3')
print(r_title.get_text())

for i in range(1,15):
    r_content = soup.select_one('#stepDiv{}'.format(i)).get_text()
    print(r_content)

for j in range(1,4):
    r_info = soup.select_one('#contents_area > div.view2_summary.st3 > div.view2_summary_info > span.view2_summary_info{}'.format(j))
    print(r_info.get_text())




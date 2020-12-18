from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import dessertDAO as dao

req = urlopen('https://www.10000recipe.com/recipe/6906441')

print(req.getcode())

if req.getcode() == 200:
    html = req.read()
    # print(html)

    html = html.decode("utf-8")
    # print(html)
else:
    print("HTTP ERROR")

soup = BeautifulSoup(html, "html.parser")
rc = ''
info = ''
rt = ''

r_title = soup.select_one('#contents_area > div.view2_summary.st3 > h3').get_text()


for i in range(1, 10):
    r_content = soup.select('.view_step > #stepDiv{}'.format(i))

    for r_contents in r_content:
      #  print(i, r_contents.get_text())
        rc = rc + r_contents.get_text()

r_info = soup.select('#contents_area > div.view2_summary.st3 > div.view2_summary_info > span')
for r_infos in r_info:
   # print(r_infos.get_text())
    info = info + r_infos.get_text()

r_img = soup.select_one('#main_thumbs')
src = r_img.attrs['src']
print(src)
#t = (r_title, rc, info)
#dao.insert(t)
#dao.select()

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import dessertDAO as dao


req = urlopen('https://www.10000recipe.com/recipe/6860385')

print(req.getcode())

if req.getcode() == 200:
    html = req.read()
    # print(html)

    html = html.decode("utf-8")
    # print(html)
else:
    print("HTTP ERROR")

soup = BeautifulSoup(html, "html.parser")
r_con = ''
info = ''
rt = ''
r_met = ''


#제목
r_title = soup.select_one('#contents_area > div.view2_summary.st3 > h3').get_text()

#조리방법
for i in range(1, 6):
    r_content = soup.select('.view_step > #stepDiv{}'.format(i))

    for r_contents in r_content:
        r_con = r_con + r_contents.get_text()
#간단정보
r_info = soup.select('#contents_area > div.view2_summary.st3 > div.view2_summary_info > span')
for r_infos in r_info:

    info = info + r_infos.get_text()

#이미지
r_img = soup.select_one('#main_thumbs')
src = r_img.attrs['src']
#print(src)


#재료
r_mete = soup.select('.ready_ingre3 > ul > a > li')
for r_metes in r_mete:
    r_met = r_met + r_metes.get_text()
#공백제거
r_mett = ' '.join(r_met.split())
print(r_mett)

t = (r_title, r_con, src,r_mett,info)
dao.insert(t)


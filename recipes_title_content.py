from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import dessertDAO as dao


req = urlopen('https://www.10000recipe.com/recipe/6935891')

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
res = soup.select_one('div.view_step')
i = 0
for r_cont in res.select('div.view_step_cont'):
    r_con = r_con + r_cont.get_text()

print(r_con)


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


t = (r_title, r_con, src,r_mett,info , 8)
dao.insert(t)

#1.떡 2.튀김 3.아이스크림 4.과일 5.야채 6.제과 7.제빵 8.기타


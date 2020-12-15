from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

req = urlopen('https://www.10000recipe.com/recipe/6943674')

print(req.getcode())

if req.getcode() == 200:
    html = req.read()
    #print(html)

    html = html.decode("utf-8")
    #print(html)
else:
    print("HTTP ERROR")

soup = BeautifulSoup(html, "html.parser")

body = soup.select("#stepDiv1 div")
body1 = soup.select("#stepDiv2 div")
body2 = soup.select("#stepDiv3 div")

print(body ,body1 ,body2 , sep='\n')
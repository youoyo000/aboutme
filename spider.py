import requests
from bs4 import BeautifulSoup
url = "https://www.atmovies.com.tw/movie/next/"
Data = requests.get(url)
Data.encoding = "utf-8"

sp = BeautifulSoup(Data.text, "html.parser")
result=sp.select(".filmListAllX li")
for item in result:

	img=item.find("img")
	print("片名:",img.get("alt"))
	print("海報",img.get("src"))
	hyperlink=item.find("a")
	a=item.find("a")
	print("介紹", "https://www.atmovies.com.tw"+ a.get("href"))
	print("編號", a.get("href")[7:19])

	div = item.find(class_ = "runtime")
	print("日期:", div.text[5:15])
	if div.text.find("片長:")>0:
		print("片長:",div.text[21:])
	else:
		print("目前無片長資訊")
	print()
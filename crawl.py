from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

baseurl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
plusurl = input('오늘의 검색어는?: ')
url = baseurl + quote_plus(plusurl)
html = urlopen(url).read()
suop = BeautifulSoup(html, 'html.parser')
img = suop.find_all(class_= '_img')
print(img[0])
n = 1

for i in img:
	imgurl = i['data-source']
	with urlopen(imgurl) as f:
		with open('./크롤링 사진' + plusurl + str(n) + '.jpg', 'wb') as h:
			img = f.read()
			h.write(img)

	n += 1
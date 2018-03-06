## 예스 24

from urllib.request import urlopen
from bs4 import BeautifulSoup

##driver.find_element_by_name('UserName').send_keys('') 아이디와 로그인이 크롬에 남아 있으므로 생략
##driver.find_element_by_name('Password').send_keys('') 이하 동문
html = urlopen('http://www.yes24.com/24/category/bestseller?CategoryNumber=001001003&sumgb=06')
rank = BeautifulSoup(html, 'html.parser')
for n in rank.find("a[href=/24/goods/34925543]"):
    n.find.parent.get_text()
    print(n)

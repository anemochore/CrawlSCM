## parser.py
import requests
from bs4 import BeautifulSoup
import re

req = requests.get('http://www.yes24.com/24/goods/31954455')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
my_titles = soup.findAll("span", {"class":"gd_sellNum"})
## my_titles는 list 객체

    ## Tag안의 텍스트
for title in my_titles:
    clean = title.text
    p = re.findall('[0-9]+', clean)

print(p)
jisu = p

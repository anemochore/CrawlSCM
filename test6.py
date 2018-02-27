## parser.py
import requests
from bs4 import BeautifulSoup
import re

req = requests.get('http://www.yes24.com/24/goods/31954455')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
my_titles = soup.select('#category_layout > tbody > tr:nth-child(3) > td.goodsTxtInfo > p:nth-child(1) > a:nth-child(1)')
## my_titles는 list 객체

    ## Tag안의 텍스트
for title in my_titles:
    print(title.get('href'))

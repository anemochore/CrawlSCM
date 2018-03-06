## 예스 24

from selenium import webdriver
from bs4 import BeautifulSoup
import datetime
import Scmcrwal
import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials

SPREAD_SHEET_NAME = "Pytest" #잠시전 생성한후 공유했던  스프레드시트의 이름입니다

json_key = json.load(open('mykey.json'))
scope = ['https://spreadsheets.google.com/feeds']

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)
gc = gspread.authorize(credentials)
fjs = gc.open(SPREAD_SHEET_NAME).sheet1

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:/Users/parkjisu/AppData/Local/Google/Chrome/User Data")  #크롬 기본 프로필을 불러옵니다. (쿠키와 아이디가 저장되어 있음)
driver = webdriver.Chrome(executable_path="C:\py\chromedriver.exe", chrome_options=options)
driver.set_window_size(1024,768) ## 크롬 창을 작게 띄웁니다.
driver.implicitly_wait(5) ## 컴이 후지니까 5초 기다립니다.

driver.get('https://scm.yes24.com/Login/LogOn')
##driver.find_element_by_name('UserName').send_keys('') 아이디와 로그인이 크롬에 남아 있으므로 생략
##driver.find_element_by_name('Password').send_keys('') 이하 동문
driver.find_element_by_xpath('//div[@class="loginBtn"]').click() ## 로그인 버튼 클릭

now = datetime.datetime.now() - datetime.timedelta(days=1) ## 타임스탬프 사용
yesterDay = now.strftime('%Y-%m-%d') ## 전일 기록을 가져오기 위해 '어제'날짜를 로드

startDate = yesterDay ##Url에 검색 시작일을 '어제' 날짜로 날짜 양식은 yyyy-mm-dd
endDate = yesterDay ##Url에 검색 종료일을 '어제' 날짜로
scmUrl = 'http://scm.yes24.com/AnalysisManagement/ListSaleAnalysisGoods/0?startDate=' + startDate + '&endDate=' + endDate + '&goodsNo='
i = 2

# 상품번호를 더하고 임의의 상품 페이지 접속 (터미널에 숫자가 뜨면 성공)
for goodsNo in Scmcrwal.yesnum:
    driver.get(scmUrl + goodsNo)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    notices = soup.select('#tbList > tr.sumtd > td.sumtd')
    for n in notices:
        print(n.text.strip())
        fjs.update_cell(i, 4, n.text.strip())
    i = i+1

driver.quit() ##웹드라이버 종료
##Yes24 판매지수

import requests
import re

i=2

for jisustack in Scmcrwal.yesnum:
    jisugoodsurl = 'http://www.yes24.com/24/goods/'+jisustack
    req = requests.get(jisugoodsurl)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    yesjisu = soup.findAll("span", {"class":"gd_sellNum"})
    for title in yesjisu:
        clean = title.text
        cleanyesjisu = re.findall('[0-9]+', clean)
    for jisu in cleanyesjisu:
        print(jisu)
        fjs.update_cell(i, 6, jisu)
    i = i+1

##crawlscm@crawlscm.iam.gserviceaccount.com

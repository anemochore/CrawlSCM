from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
# options.add_argument("user-data-dir=C:/Users/parkjisu/AppData/Local/Google/Chrome/User Data")  #크롬 기본 프로필을 불러옵니다. (쿠키와 아이디가 저장되어 있음)
driver = webdriver.Chrome(executable_path="./chromedriver.exe", chrome_options=options)
driver.set_window_size(1024,768) ## 크롬 창을 작게 띄웁니다.
driver.implicitly_wait(3) ## 컴이 후져도 3초 기다립니다.
driver.get('https://scm.kyobobook.co.kr/scm/login.action')
driver.find_element_by_id('ipt_userId').send_keys('2208105665')
driver.find_element_by_id('ipt_password').send_keys('hanbit0319319!')
driver.find_element_by_xpath('//*[@id="btn_login"]').click() ## 로그인 버튼 클릭
driver.implicitly_wait(3) ## 컴이 후져도 또한 10초 기다립니다.

# driver.get('https://scm.kyobobook.co.kr/scm/page.action?pageID=main')

WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "s_vndrList_label")))
driver.execute_script("document.getElementById('s_vndrList_label').click();")

WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "s_vndrList_itemTable")))
driver.execute_script("document.getElementById('s_vndrList_itemTable_1').click();")

now = datetime.datetime.now() - datetime.timedelta(days=1) ## 타임스탬프 사용
yesterDay = now.strftime('%Y%m%d') ## 전일 기록을 가져오기 위해 '어제'날짜를 로드
startDate = yesterDay ##Url에 검색 시작일을 '어제' 날짜로 날짜 양식은 yyyymmdd
endDate = yesterDay ##Url에 검색 종료일을 '어제' 날짜로
# 상품번호와 전일 날짜를 각각의 폼에 전송하고 조회 (터미널에 숫자가 뜨면 성공)

i = 2

for goodsNo in Scmcrwal.kyobonum:
    driver.get('https://scm.kyobobook.co.kr/scm/page.action?pageID=saleStockInfo') ## 판매조회 페이지로 이동
    driver.find_element_by_id('sel_strDateTo_input').send_keys(endDate) ## 종료기간 폼에 입력
    driver.find_element_by_id('sel_strDateFrom_input').clear()
    driver.find_element_by_id('sel_strDateFrom_input').send_keys(startDate) ## 시작기간 폼에 입력
    driver.find_element_by_id('sel_cmdtCode').send_keys(goodsNo) ## 상품명에 ISBN 입력
    driver.find_element_by_id('btn_search').click() ## [조회]버튼 클릭
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "grd_saleStockInfo_cell_0_6")))
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    koffline = soup.select('#grd_saleStockInfo_cell_0_6 > nobr') ## 판매(영업점) 기록 파싱
    for x in koffline:
        print(x.text)
        fjs.update_cell(i, 7, x.text)
    konline = soup.select('#grd_saleStockInfo_cell_0_7 > nobr') ## 판매(영업점) 기록 파싱
    for y in konline:
        print(y.text)
        fjs.update_cell(i, 8, y.text)
    i = i+1

##driver.quit() ##웹드라이버 종료

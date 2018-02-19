from selenium import webdriver
from bs4 import BeautifulSoup
import datetime

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:/Users/parkjisu/AppData/Local/Google/Chrome/User Data")  #크롬 기본 프로필을 불러옵니다. (쿠키와 아이디가 저장되어 있음)
driver = webdriver.Chrome(executable_path="C:\py\chromedriver.exe", chrome_options=options)
driver.set_window_size(800,600) ## 크롬 창을 작게 띄웁니다.
driver.implicitly_wait(5) ## 컴이 후지니까 5초 기다립니다.

driver.get('https://scm.yes24.com/Login/LogOn')
##driver.find_element_by_name('UserName').send_keys('jthhke') 아이디와 로그인이 크롬에 남아 있으므로 생략
##driver.find_element_by_name('Password').send_keys('hanbit0319319!!') 이하 동문
driver.find_element_by_xpath('//div[@class="loginBtn"]').click() ## 로그인 버튼 클릭

now = datetime.datetime.now() - datetime.timedelta(days=1) ## 타임스탬프 사용
yesterDay = now.strftime('%Y-%m-%d') ## 전일 기록을 가져오기 위해 '어제'날짜를 로드

startDate = yesterDay ##Url에 검색 시작일을 '어제' 날짜로 날짜 양식은 yyyy-mm-dd
endDate = yesterDay ##Url에 검색 종료일을 '어제' 날짜로
scmUrl = 'http://scm.yes24.com/AnalysisManagement/ListSaleAnalysisGoods/0?startDate=' + startDate + '&endDate=' + endDate + '&goodsNo='

# 상품번호를 더하고 임의의 상품 페이지 접속 (터미널에 숫자가 뜨면 성공)
goodsNo = "55864765" ##상품번호
driver.get(scmUrl + goodsNo)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
notices = soup.select('#tbList > tr.sumtd > td.sumtd')

for n in notices:
    print(n.text.strip())

goodsNo = "58100107" ##상품번호
driver.get(scmUrl + goodsNo)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
notices = soup.select('#tbList > tr.sumtd > td.sumtd')

for n in notices:
    print(n.text.strip())

driver.quit() ##웹드라이버 종료

##구글 스프레드 시트 테스트

import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials

SPREAD_SHEET_NAME = "Pytest" #잠시전 생성한후 공유했던  스프레드시트의 이름입니다

json_key = json.load(open('mykey.json'))
scope = ['https://spreadsheets.google.com/feeds']

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)

gc = gspread.authorize(credentials)

##wks = gc.open(SPREAD_SHEET_NAME).sheet1
##wks.update_acell('A1', test4.jisu)
##wks.update_acell('A2', test6.rank)

fjs = gc.open(SPREAD_SHEET_NAME).sheet1
kuda = fjs.cell(2, 2).value
print(kuda)

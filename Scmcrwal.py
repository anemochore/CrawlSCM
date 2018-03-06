##구글 스프레드 시트 테스트

import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials

SPREAD_SHEET_NAME = "Pytest" #잠시전 생성한후 공유했던  스프레드시트의 이름입니다

json_key = json.load(open('mykey.json'))
scope = ['https://spreadsheets.google.com/feeds']

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)
gc = gspread.authorize(credentials)

fyes = gc.open(SPREAD_SHEET_NAME).sheet1
yesnum = [item for item in fyes.col_values(2) if item]
print(yesnum)
kyobonum = [item for item in fyes.col_values(3) if item]
print(kyobonum)

##def yesnumstack():
##    for yespro in yesnum:

def yessellstack(i):
    fjs.update_cell(i, 4, n.text.strip())

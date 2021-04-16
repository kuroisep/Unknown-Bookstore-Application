import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('minor1981-a976b13f378a.json')

gc = gspread.authorize(credentials)

wks = gc.open('Table').sheet1

print(wks.get_all_records())
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from market_data import *
import time
from datetime import datetime

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name('google_credentials.json', scope)
client = gspread.authorize(credentials)

spreadsheet = client.open('Stock Screener')

while True:
    create_df(sp500_symbols)
    with open('export_dataframe.csv', 'r') as file_obj:
        content = file_obj.read()
        client.import_csv(spreadsheet.id, data=content)
    now = datetime.now()
    current_time = now.strftime("%d/%m/%Y %H:%M:%S")
    print("Updated at: ", current_time)
    time.sleep(30)
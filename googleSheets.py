import pandas as pd
import gspread
from df2gspread import df2gspread as d2g
from oauth2client.service_account import ServiceAccountCredentials


def sheetsUpload(csvFile, sheetName):
    data = pd.read_csv(csvFile)
    df = pd.DataFrame(data)

    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name('leadgeneration-279518-e675ca0bb2bf.json', scope)

    gc = gspread.authorize(credentials)

    spreadsheet_key = '1afCl7FJ4UMoRFCibRTUXdzqT-XsiUOl5hfHNnYkbMO8'
    wks_name = sheetName

    d2g.upload(df, spreadsheet_key, wks_name, credentials=credentials, row_names=True)



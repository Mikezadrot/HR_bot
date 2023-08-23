import gspread
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv
import os

load_dotenv()


def connect_to_google_sheet():
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = Credentials.from_service_account_file('creds.json', scopes=scope)
    client = gspread.authorize(creds)
    return client


def get_data_from_spreadsheet():

    client = connect_to_google_sheet()

    worksheet = client.open_by_key(os.getenv('SPREADSHEET_ID')).sheet1
    data = worksheet.get_all_values()
    print(data)
    return data


def list_existing_sheets(clients, spreadsheets_id):
    spreadsheet = clients.open_by_key(spreadsheets_id)
    sheet_names = [worksheet.title for worksheet in spreadsheet.worksheets()]
    return sheet_names


def open_tab(spreadsheets_id, sheets_name):

    spreadsheet = client.open_by_key(spreadsheets_id)
    worksheet = spreadsheet.worksheet(sheets_name)
    data = worksheet.get_all_values()
    for row in data:
        print(row)


def existing_sheets():
    ex = list_existing_sheets(client, spreadsheet_id)
    print("Список існуючих листів:")
    for sheet_name in ex:
        print(sheet_name)
        open_tab(spreadsheet_id, sheet_name)


client = connect_to_google_sheet()
spreadsheet_id = os.getenv('SPREADSHEET_ID')
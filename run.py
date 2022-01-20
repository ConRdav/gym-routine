import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('gym_routine')

three_day_routine = SHEET.worksheet('three')
four_day_routine = SHEET.worksheet('four')
five_day_routine = SHEET.worksheet('five')

data_1 = three_day_routine.get_all_values()
data_2 = four_day_routine.get_all_values()
data_3 = five_day_routine.get_all_values()

print(data_1)
print(data_2)
print(data_3)

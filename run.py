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

def get_workout_routine():
    """
    Gets the workout routine requested by the user
    """
    print("Please choose a workout routine.")
    print("Your options are a 3 day, 4 day or 5 day routine.")
    print("Please choose your preferred routine by entering 3,4 or 5.\n")

    routine = input("Enter your choice here: ")
    print(f"You have chosen the {routine} day workout routine")

get_workout_routine()

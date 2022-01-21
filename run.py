import gspread
from google.oauth2.service_account import Credentials
import re
from pprint import pprint


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
    while True:
        print("Please choose a workout routine.")
        print("Your options are a 3 day, 4 day or 5 day routine.")
        print("Please choose your preferred routine by entering 3, 4 or 5.\n")

        routine = input("Enter your choice here: ")
        if validate_routine(routine):
            print(f"You picked the {routine} day workout routine.")
            break
        else:
            print("Invalid entry, please enter 3, 4 or 5.")

    show_routine(routine)

def validate_routine(routine):
    """
    validates the user input
    """
    pattern = re.compile('[3-5]{1}')
    return pattern.match(routine)
    
def show_routine(routine):
    if routine == '3':
        pprint(three_day_routine.get_all_values())
    elif routine == '4':
        pprint(four_day_routine.get_all_values())
    else:
        pprint(five_day_routine.get_all_values())

def main():
    """
    runs the app
    """
    workout_routine = get_workout_routine()

print("Welcome to the Gym Routine!")
main()
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
workouts = SHEET.worksheet('workouts')


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

def get_input(prompt = "", cast = None, condition = None, errorMessage = None):
    while True:
        try: 
            response = (cast or str)(input(prompt))
            assert condition is None or condition(response)
            return response
        except:
            print(errorMessage or "Invalid input. Try again.")





def create_own_workout():
    print("Create your own workout.\n")
    new_workout = get_input(prompt = "Name your workout: ")
    print("You are limited to 4 exercises to pick carefully!\n")
    create_exercise1 = get_input(prompt = "Enter your exercise name: ")
    create_exercise2 = get_input(prompt = "Enter your exercise name: ")
    create_exercise3 = get_input(prompt = "Enter your exercise name: ")
    create_exercise4 = get_input(prompt = "Enter your exercise name: ")
    print("Now enter the workouts sets and reps.")
    print("You are limited to numbers 1-9.\n")
    create_sets = get_input(prompt = "Enter the amount of sets per exercise: ", cast = int)
    create_reps = get_input(prompt = "Enter the amount of reps per exercise: ", cast = int)
    print("Well done you have created your own workout!\n")
    print("If you would like to view your workout press V or to create a new one press C.\n")
    data = [[new_workout, create_exercise1, create_exercise2, create_exercise3, create_exercise4, create_sets, create_reps]]
    update_workouts(data)

def update_workouts(data):
    print("Updating Workout Database...\n")
    workouts.insert_rows(data)
    print("Workout succesfully added to Workout Database.")

def view_workouts():
     pprint(workouts.get_all_values())
     
def main():
    """
    runs the app
    """
    if input == 'P':
        get_workout_routine()
    elif input == 'C':
        create_own_workout()
    else:
        view_workouts()
    
   
print("Welcome to the Gym Routine!\n")
print("To pick a routine press P.\n")
print("To create own workout press C.\n")
print("To view the workout database press V.\n")
input("Enter your choice here: ")
main()
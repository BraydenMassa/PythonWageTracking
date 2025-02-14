import json
from json import JSONDecodeError
from IPython.display import clear_output

from Shift import Shift
from ShiftRepository import ShiftRepository
from helpers import is_valid_int, is_valid_float

# Static functions
def get_input(prompt, validate, error_message="Invalid input. Please try again"):
    while True:
        result = input(prompt)
        if validate(result):
            return result
        clear_output()
        print(error_message)

def get_int_input(prompt):
    return int(get_input(prompt, is_valid_int, "Invalid input. Please enter a whole number"))

def get_str_input(prompt):
    return get_input(prompt, lambda x: bool(x.strip()), "Please enter an input")

def get_float_input(prompt):
    return float(get_input(prompt, is_valid_float, "Invalid input. Please enter a number"))

def get_specific_input(prompt, valid_options):
    return get_input(prompt, lambda x: x in valid_options)

def get_workplace_data():
    data = {}
    with open("workplaces.json", "r") as file:
        try:
            data = json.load(file)
        except JSONDecodeError:
            pass
    if data:
        return data
    num_workplaces = get_int_input("How many places do you work?: ")
    for i in range(1, num_workplaces + 1):
        location_name = get_str_input(f"Please enter name of job {i}: ")
        base_pay = get_float_input(f"What is your base wage at {location_name}? ($/hr): ")
        data[location_name] = base_pay
    with open("workplaces.json", "w") as file:
        json.dump(data, file)
    return data

# App class to run main loop
class App:
    VALID_INPUTS = ['1', '2', '3', '4', '5', '6']
    def __init__(self, db_connection_string):
        print("Welcome to the Wage Tracking App!\n")
        self.workplaces_err = ""
        self.shift_repo = ShiftRepository(db_connection_string)
        self.workplaces = self.get_workplace_data()
        self.main_loop()

    # Main loop
    def main_loop(self):
        clear_output()
        print("Welcome to the Wage Tracking App!\n")
        while True:
            user_input = input(self.display_options())
            if user_input not in self.VALID_INPUTS:
                clear_output()
                print(f"Invalid input. Please only enter a number ({self.VALID_INPUTS[0]}-{self.VALID_INPUTS[-1]})")
                continue
            clear_output()
            if user_input == '1':
                self.display_shifts()
            elif user_input == '2':
                self.add_shift()
            elif user_input == '3':
                self.delete_shift()
            elif user_input == '4':
                self.display_statistics()
            elif user_input == '5':
                self.display_settings()
            else:
                clear_output()
                print("Thanks for using the Wage Tracking app. See you later!")
                break

    # Method to view shifts
    def display_shifts(self):
        self.print_header("Shifts")
        shifts = [str(shift) for shift in self.shift_repo.get_all_shifts()]
        if len(shifts) == 0:
            print("No shifts to display.")
        else:
            for shift in shifts:
                print(shift + '\n')

    # Helper method to get user input while adding a shift
    def get_shift_input(self, category, is_shift_type=False):
        temp = None
        if category == "hours":
            print("(To cancel, enter 'x')\n" + '*' * 22)

        while temp is None:
            temp = input(f"Enter {category}: ")
            if temp.lower() == 'x':
                clear_output()
                print("Operation cancelled successfully.")
                return "cancel"
            if is_shift_type:
                if temp not in ["s", "b", "S", "B"]:
                    print("Invalid shift type, please enter a 'b' for bartender, or 's' for server")
                    temp = None
                else:
                    return temp
            elif is_valid_float(temp):
                return float(temp)
            else:
                print("Invalid number, please enter a valid number.")
                temp = None

    # Method to add shift to the database
    def add_shift(self):
        self.print_header("Add Shift")
        hours = card = cash = shift_type = None

        hours = self.get_shift_input("hours")
        if hours == "cancel":
            return
        card = self.get_shift_input("card tips")
        if card == "cancel":
            return
        cash = self.get_shift_input("cash tips")
        if cash == "cancel":
            return
        shift_type = self.get_shift_input("shift type - (s) for server, or (b) for bartender", True)
        if shift_type == "cancel":
            return

        new_shift = Shift(hours, card, cash, "Server" if shift_type == "s" else "Bartender", self.base_pay)
        add_result = self.shift_repo.add_shift(new_shift)
        clear_output()
        if add_result is None:
            print("Unknown error adding shift. Please try again later.")
        else:
            print("Shift added successfully")

    # Method to delete a shift
    def delete_shift(self):
        self.print_header("Delete a Shift")
        shifts = self.shift_repo.get_all_shifts()
        if len(shifts) == 0:
            print("No shifts to delete.")
            return

        to_delete = None
        while to_delete is None:
            for i in range(len(shifts)):
                print(f"[{i + 1}] {shifts[i]}\n")
            print("(To cancel, enter 'x')\n" + '*' * 22)
            to_delete = input("Enter the shift you would like to delete: ")
            if to_delete == 'x' or to_delete == 'X':
                clear_output()
                print("Operation cancelled successfully.")
                return
            valid_inputs = [i for i in range(1, len(shifts) + 1)]

            if not is_valid_int(to_delete):
                print("Invalid input. Please enter the number of the shift you want to delete.")
                to_delete = None
                continue

            if int(to_delete) not in valid_inputs:
                clear_output()
                print("Invalid input. Please enter the number of the shift you want to delete.")
                to_delete = None
                continue
        to_delete = int(to_delete) - 1
        clear_output()
        if self.shift_repo.delete_shift(shifts[to_delete]._id):
            print("Shift deleted successfully")
        else:
            print("Unknown error deleting shift. Please try again later.")

    # Method to display Statistics
    def display_statistics(self):
        shifts = self.shift_repo.get_all_shifts()
        stats_calc = StatisticsCalculator(shifts)
        server_calc = StatisticsCalculator(stats_calc.serving_shifts())
        bartender_calc = StatisticsCalculator(stats_calc.bartending_shifts())
        self.print_header("Statistics")
        print("\n" + '*' * 38)
        print("Overall:\n")
        print(f"Total hours worked: {stats_calc.total_hours()}")
        print(f"Total money made: ${stats_calc.total_money()}")
        print(f"Average hourly rate: ${stats_calc.total_hourly_rate()}/hr")
        print("*" * 38)
        print("Serving:\n")
        print(f"Serving hours worked: {server_calc.total_hours()}")
        print(f"Total money made serving: ${server_calc.total_money()}")
        print(f"Average hourly rate serving: ${server_calc.total_hourly_rate()}")
        print("*" * 38)
        print("Bartending:\n")
        print(f"Bartending hours worked: {bartender_calc.total_hours()}")
        print(f"Total money made bartending: ${bartender_calc.total_money()}")
        print(f"Average hourly rate bartending: ${bartender_calc.total_hourly_rate()}")
        print("*" * 38 + "\n")

    def display_settings(self):
        self.print_header("Settings")
        selected = None
        while selected is None:
            self.display_setting_options()
            selected = input("Please select a setting")
            if selected not in ['1', '2']:
                clear_output()
                selected = None
                print("Invalid input. Please enter a number [1-2]")
                continue
            if selected == '1':
                clear_output()
                update_job_input = None
                while update_job_input == None:
                    print("\nPlease select an option below:")
                    print("[1] Update a job")
                    print("[2] Delete a job")
                    print("[3] Exit")
                    update_job_input = input("Your selection: ")
                    if update_job_input not in ['1', '2', '3']:
                        update_job_input = None
                        clear_output()
                        print("Invalid input.")



            else:
                clear_output()
                break

    def display_jobs(self):
        locations = list(self.workplaces.keys())
        for i in range(1, len(locations) + 1):
            location = locations[i]
            print(f"[i] {location}. Base Pay: ${self.workplaces[location]}/hr)")


def display_setting_options(self):
    print("[1] Update job information")
    print("[2] Exit settings")


def display_options(self):
    return '*' * 19 + '\n' + "[1] View Shifts\n[2] Add New Shift\n[3] Delete a Shift\n[4] View Statistics\n[5] Settings\n[6] Quit\n" + '*' * 19 + '\n'


def print_header(self, title):
    print(f"\n{title}\n" + '-' * len(title))


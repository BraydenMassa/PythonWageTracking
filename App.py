from ShiftRepository import ShiftRepository
from operations.AddShift import add_shift
from operations.DeleteShift import delete_shift
from operations.DisplaySettings import display_settings
from operations.DisplayShifts import display_shifts
from operations.DisplayStatistics import display_statistics
from utils.helpers import clear_output

class App:
    VALID_INPUTS = ['1', '2', '3', '4', '5', '6']
    def __init__(self, db_connection_string):
        self.shift_repo = ShiftRepository(db_connection_string)
        self.main_loop()

    # Main loop
    def main_loop(self):
        clear_output()
        print("Wage Tracker\n")
        while True:
            user_input = input(display_main_menu())
            if user_input not in self.VALID_INPUTS:
                clear_output()
                print(f"Invalid input. Please only enter a number ({self.VALID_INPUTS[0]}-{self.VALID_INPUTS[-1]})")
                continue
            clear_output()
            if user_input == '1':
                display_shifts(self.shift_repo.get_all_shifts())
            elif user_input == '2':
                add_shift(self.shift_repo)
            elif user_input == '3':
                delete_shift(self.shift_repo)
            elif user_input == '4':
                display_statistics(self.shift_repo)
            elif user_input == '5':
                display_settings()
            else:
                display_goodbye()
                break

# Displays main menu of application
def display_main_menu():
    return '*' * 19 + '\n' + "[1] View Shifts\n[2] Add New Shift\n[3] Delete a Shift\n[4] View Statistics\n[5] Settings\n[6] Quit\n" + '*' * 19 + '\n\nEnter input: '

# Executed when program ends
def display_goodbye():
    print("*" * 56 + "\n")
    print("Thank you for using the Wage Tracking app. See you soon!\n")
    print("*" * 56 + "\n")

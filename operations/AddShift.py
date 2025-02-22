# Helper method to get user input while adding a shift
from IPython.core.display_functions import clear_output

from Shift import Shift
from operations.StaticOperations import print_header
from utils.helpers import is_valid_float


def get_shift_input(category, is_shift_type=False):
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
def add_shift(shift_repo):
    print_header("Add Shift")
    hours = card = cash = shift_type = None

    hours = get_shift_input("hours")
    if hours == "cancel":
        return
    card = get_shift_input("card tips")
    if card == "cancel":
        return
    cash = get_shift_input("cash tips")
    if cash == "cancel":
        return
    shift_type = get_shift_input("shift type - (s) for server, or (b) for bartender", True)
    if shift_type == "cancel":
        return

    new_shift = Shift(hours, card, cash, "Server" if shift_type == "s" else "Bartender", self.base_pay)
    add_result = shift_repo.add_shift(new_shift)
    clear_output()
    if add_result is None:
        print("Unknown error adding shift. Please try again later.")
    else:
        print("Shift added successfully")

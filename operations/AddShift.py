from utils.helpers import clear_output, get_todays_date
from Shift import Shift
from operations.StaticOperations import get_date_input, print_header, get_basepay
from utils.helpers import is_valid_float

# Helper method to get user input while adding a shift
def get_shift_input(category, date, is_shift_type=False):
    temp = None
    if category == "hours":
        print(f"Adding shift on {date}")
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
    date_input = get_date_input("Enter the date of the shift in MM/DD/YYYY\nformat, or press enter if the shift was today: ")
    shift_date = get_todays_date() if date_input == -1 else date_input
    clear_output()
    print_header("Add Shift")
    hours = get_shift_input("hours", shift_date)
    if hours == "cancel":
        return
    card = get_shift_input("card tips", shift_date)
    if card == "cancel":
        return
    cash = get_shift_input("cash tips", shift_date)
    if cash == "cancel":
        return
    shift_type = get_shift_input("shift type - (s) for server, or (b) for bartender", shift_date, True)
    if shift_type == "cancel":
        return

    new_shift = Shift(hours=hours, 
                      card_tips=card, 
                      cash_tips=cash, 
                      shift_type="Server" if shift_type == "s" else "Bartender", 
                      base_pay=get_basepay(),
                      date=shift_date)
    add_result = shift_repo.add_shift(new_shift)
    clear_output()
    if add_result is None:
        print("Unknown error adding shift. Please try again later.")
    else:
        print("Shift added successfully")

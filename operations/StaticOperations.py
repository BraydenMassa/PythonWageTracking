from utils.helpers import clear_output, is_valid_date
from utils.helpers import is_valid_int, is_valid_float

# Generic get_input method, can be provided validate function to
# loop until specified condition is met
def get_input(prompt, validate, error_message="Invalid input. Please try again"):
    while True:
        result = input(prompt)
        if validate(result):
            return result
        clear_output()
        print(error_message)

# Gets and returns integer input as int
def get_int_input(prompt):
    return int(get_input(prompt, is_valid_int, "Invalid input. Please enter a whole number"))

# Gets and returns string input
def get_str_input(prompt):
    return get_input(prompt, lambda x: bool(x.strip()), "Please enter an input")

# Gets and returns float input as float
def get_float_input(prompt):
    return float(get_input(prompt, is_valid_float, "Invalid input. Please enter a number"))

# Gets and returns date input as string MM/DD/YY
def get_date_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input == '':
            return -1
        if is_valid_date(user_input):
            return user_input
        clear_output()
        print("Invalid date.")
        
# Gets input that is included in valid_options list and returns it
def get_specific_input(prompt, valid_options):
    return get_input(prompt, lambda x: x in valid_options)

# Prints header for an operation
def print_header(title):
    print(f"\n{title}\n" + '-' * len(title))

# Retrieves base pay from BasePay.txt
def get_basepay():
    with open("BasePay.txt", "r") as file:
        pay = file.read()
    if not is_valid_float(pay):
        raise ValueError("Base pay file can only contain a number")
    return float(pay)
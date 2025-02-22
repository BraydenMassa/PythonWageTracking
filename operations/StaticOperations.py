from json import JSONDecodeError
from IPython.display import clear_output
import json
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

# Gets input that is included in valid_options list and returns it
def get_specific_input(prompt, valid_options):
    return get_input(prompt, lambda x: x in valid_options)

# Function to retrieve workplace data from BasePay.txt,
# or prompt user for it if it does not exist
def get_workplace_data():
    data = {}
    with open("BasePay.txt", "r") as file:
        try:
            data = json.load(file)
        except JSONDecodeError:
            # First time user has opened app, so user will be
            # prompted to enter it
            pass
    # If there is data, 'BasePay.txt' should be populated,
    # So this data can be returned
    if data:
        return data

    # Prompts user for workplace info and sets it to the data object
    num_workplaces = get_int_input("How many places do you work?: ")
    for i in range(1, num_workplaces + 1):
        location_name = get_str_input(f"Please enter name of job {i}: ")
        base_pay = get_float_input(f"What is your base wage at {location_name}? ($/hr): ")
        data[location_name] = base_pay
    # Writes this data to the json file for future use
    with open("BasePay.txt", "w") as file:
        json.dump(data, file)
    return data

# Prints header for an operation
def print_header(title):
    print(f"\n{title}\n" + '-' * len(title))


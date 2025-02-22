import os
from datetime import datetime

def is_valid_int(num):
    try:
        int(num)
        return True
    except ValueError as e:
        return False

def is_valid_float(num):
    try:
        float(num)
        return True
    except ValueError as e:
        return False
    
def clear_output():
    os.system("cls" if os.name == "nt" else "clear")

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%m/%d/%Y")
        return True
    except ValueError:
        return False
    
def get_todays_date():
    return datetime.now().strftime("%m/%d/%Y")
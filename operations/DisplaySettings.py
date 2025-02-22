from IPython.core.display_functions import clear_output
from operations.StaticOperations import print_header, get_float_input


# Displays settings screen
def display_settings():
    print_header("Settings")
    selected = None
    while selected is None:
        display_setting_options()
        selected = input("Please select a setting: ")
        if selected not in ['1', '2', '3']:
            clear_output()
            selected = None
            print("Invalid input. Please enter a number [1-2]")
            continue
        if selected == '1':
            clear_output()
            with open("BasePay.txt", "r") as file:
                base_pay = file.read()
            print(f"Current Base Pay: {base_pay}")
            selected = None
        elif selected == '2':
            clear_output()
            updated_base_pay = get_float_input("Enter base pay")
            with open("BasePay.txt", "w") as file:
                file.write(str(updated_base_pay))
            selected = None
            print(f"Base pay updated to {updated_base_pay}")
        else:
            clear_output()
            break

def display_jobs(workplaces):
    locations = list(workplaces.keys())
    for i in range(1, len(locations) + 1):
        location = locations[i]
        print(f"[i] {location}. Base Pay: ${workplaces[location]}/hr)")


def display_setting_options():
    print("[1] View Base Pay")
    print("[2] Update Base Pay")
    print("[3] Exit settings")


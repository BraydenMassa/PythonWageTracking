# Function to delete a shift
from IPython.core.display_functions import clear_output
from operations.StaticOperations import print_header
from utils.helpers import is_valid_int


def delete_shift(shift_repo):
    print_header("Delete a Shift")
    shifts = shift_repo.get_all_shifts()
    if len(shifts) == 0:
        print("No shifts to delete.")
        return

    to_delete = get_shift_to_delete(shifts)
    clear_output()
    if shift_repo.delete_shift(shifts[to_delete].get_id):
        print("Shift deleted successfully")
    else:
        print("Unknown error deleting shift. Please try again later.")

def get_shift_to_delete(shifts):
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
        # Returns to_delete - 1 because array is indexed at 0
        return int(to_delete) - 1
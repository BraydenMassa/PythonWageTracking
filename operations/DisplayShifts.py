from operations.StaticOperations import print_header
import pandas as pd
from tabulate import tabulate

# Function to display all shifts to user
def display_shifts(shifts):
    print_header("Shifts")

    if len(shifts) == 0:
        print("No shifts to display.")
    shift_data = [shift.to_dict() if hasattr(shift, 'to_dict') else shift for shift in shifts]
    df = pd.DataFrame(shift_data)
    table = tabulate(df, headers='keys', tablefmt='grid', numalign='right', stralign='center', showindex=False)
    print(f'\n\n{table}\n')

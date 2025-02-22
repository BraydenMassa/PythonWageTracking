from operations.StaticOperations import print_header

# Function to display all shifts to user
def display_shifts(shifts):
    print_header("Shifts")
    shifts = [str(shift) for shift in shifts]
    if len(shifts) == 0:
        print("No shifts to display.")
    else:
        for shift in shifts:
            print(shift + '\n')

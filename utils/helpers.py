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

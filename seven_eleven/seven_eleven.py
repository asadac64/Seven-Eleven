"""Print Seven-Eleven"""

def print_7_eleven(num):
    if num % 7 == 0:
        return "Seven"
    if num % 11 == 0:
        return "Eleven"
    if num % 7 == 0 and num % 11 == 0:
        return "7-Eleven"
    else:
        return "Error"
"""
File: subtract_numbers.py
-------------------------
This program gets two real-values from the user and prints
the first number minus the second number.
"""


def main():
    """
    def subtract_numbers: Created to read two real numbers from the user and prints the first number minus the second.
    variable 1 - number_1 = First Number
    variable 2 - number_2 = Second Number
    variable 3 - result = The first number minus the second number
    """
    subtract_numbers()

def subtract_numbers():
    number_1 = float(input('First Number: '))
    number_2 = float(input('Second Number: '))
    result = number_1 - number_2
    print('The result is', result)

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()

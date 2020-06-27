"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""

import random


def main():
    """
    generate_two_digit_integers(): Created to generate simple addition problems that involve adding two 2-digit integers
    while loop: just ends when the user gets 3 correct answers.
    corrects = count the numbers of correct answers.
    user_answer = the answer of the user.
    """
    generate_two_digit_integers()

def generate_two_digit_integers():
    corrects = 0
    while corrects != 3:
        number_1 = random.randint(10, 99)
        number_2 = random.randint(10, 99)
        result = number_1 + number_2
        print(f'What is {number_1} + {number_2} ?')
        user_answer = int(input('Your answer: '))
        if user_answer == result:
            corrects += 1
            print(f'Correct! You have gotten {corrects} in a row.')
        else:
            print(f'Incorrect. The expected answer is {result}.')
    print('Congratulations! You mastered addition.')

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()

"""
File: random_numbers.py
-----------------------
This program prints a series of random numbers in the
range from MIN_RANDOM to MAX_RANDOM, inclusive
"""

import random

def main():
    """
    generate_ten_numbers(): Created to generate 10 random numbers between 0 and 100, inclusive.
    MIN_RANDOM = 0
    MAX_RANDOM = 100
    for loop to generate 10 numbers using NUM_RANDOM.
    """
    generate_ten_numbers()

def generate_ten_numbers():
        MIN_RANDOM = 0
        MAX_RANDOM = 100
        for c in range(0, 10):
            NUM_RANDOM = random.randint(MIN_RANDOM, MAX_RANDOM)
            print(NUM_RANDOM)
# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()

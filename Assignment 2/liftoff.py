"""
File: liftoff.py
----------------------
This program writes out the calls for a spaceship that is about to launch.
It counts down the numbers from 10 to 1 and then writes “Liftoff!”
"""


def main():
    """
    liftoff(): Created to countdown the numbers from 10 to 1 and then write "Liftoff!" using a for loop
    """
    liftoff()

def liftoff():
   for c in range(11, 1, -1):
       c -= 1
       print(c)
   print('Liftoff!')

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()

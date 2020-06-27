from karel.stanfordkarel import *

"""
File: ExtensionKarel.py
-----------------------
This file is for optional extension programs. 
"""

def main():
    """
    karel starts at (1,1) facing east
    """
    size_of_the_world()






def size_of_the_world():
    count_row = count_column = 1
    while front_is_clear():
        move()
        count_row += 1
    if front_is_blocked():
        turn_left()
        while front_is_clear():
            move()
            count_column += 1
        if front_is_blocked():
            return_to_the_start()
            print(f'World {count_column} X {count_row}')
            # pre condition to continue run the program
            if count_row < 20 or count_column < 20:
                print('This world is so small to Karel generate her message, please try again!')
            else:
                print('Okay!, Let´s start!')



def return_to_the_start():
    turn_right()
    turn_right()
    while front_is_clear():
        move()
    turn_right()
    while front_is_clear():
        move()
    if front_is_blocked():
        turn_right()
        turn_right()


def turn_right():
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()

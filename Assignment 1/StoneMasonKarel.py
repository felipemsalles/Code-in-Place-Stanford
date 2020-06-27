from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
    """
    function complete_with_beepers(): Created to repair the problem putting beepers on the columns.
    function up_walls(): Created to analyze if the front of Karel is blocked or not in the up positions of the columns.
    function down_walls(): Created to analyze if the front of Karel is blocked or not in the up positions of the columns.
    function check_walls(): Created to analyze if there is a wall or not in certain position.
    function turn_right(): Created to Karel turn right.
    """
    turn_left()#1 column
    complete_with_beepers()
    up_walls()
    move_to_next_column()
    check_walls()#5 column
    turn_right()
    turn_right()
    complete_with_beepers()
    down_walls()
    move_to_next_column()
    check_walls()#9 column
    up_walls()
    move_to_next_column()
    check_walls()
    up_walls()
    complete_with_beepers()
    turn_right()
    complete_with_beepers()

def complete_with_beepers():
    while not front_is_blocked():
        if no_beepers_present():
            put_beeper()
            move()
        else:
            move()
    if front_is_blocked():
        if no_beepers_present():
            put_beeper()

def check_walls():
    turn_left()
    complete_with_beepers()

def up_walls():
    if front_is_blocked():
        turn_right()

def down_walls():
    if front_is_blocked():
        turn_left()

def move_to_next_column():
    move()
    move()
    move()
    move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()

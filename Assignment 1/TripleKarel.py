from karel.stanfordkarel import *

"""
File: TripleKarel.py
--------------------
When you finish writing this file, TripleKarel should be
able to paint the exterior of three buildings in a given
world, as described in the Assignment 1 handout. You
should make sure that your program works for all of the 
Triple sample worlds supplied in the starter folder.
"""


def main():
    """
    function paint_building: Created to put beepers around the buildings.
    turn_around_left(): Created to turn Karel around the building to the left.
    turn_around_right(): Created to turn Karel around the building to the right.
    right_condition(): Created to determinate a right condition to Karel goes to another position.
    turn_right(): Created to turn Karel to the right position.
    """
    for c in range(2):
        paint_building()
        turn_around_left()
    right_condition()
    for w in range(2):
        paint_building()
        turn_around_left()
    right_condition()
    for p in range(2):
        paint_building()
        turn_around_left()
    paint_building()

def paint_building():#function to put beepers around the buildings.
    while left_is_blocked():
        put_beeper()
        move()

def turn_around_left():#turn around the building to the left.
    turn_left()
    move()

def turn_around_right():#turn around the building to the right.
    turn_right()
    put_beeper()
    move()

def right_condition():#right condition to Karel goes to another position.
    paint_building()
    turn_around_right()

def turn_right():#function to turn Karel to the right position.
    turn_left()
    turn_left()
    turn_left()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()

from karel.stanfordkarel import * 

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    """
    MidpointKarel Summary
    function world_1x1_and_2x2_and_3x5(): Created to control 3 types of situations.
    function world_5x5_and_7x7_and_10x8(): Created to control 3 types of situations.
    function return_to_center: Return Karel to the Center of First Row 5x5.
    function return_to_center_10x8_or_7x7(): #return to the center of first row of 10x8 world or 7x7 world.
    """
    world_1x1_and_2x2_and_3x5()
    world_5x5_and_7x7_and_10x8()

def world_1x1_and_2x2_and_3x5():
    if front_is_blocked():  #condition to the world Midpoint1.
        put_beeper()
    else:  #condition to the world Midpoint2.
        move()
        if front_is_blocked():
            put_beeper()
        else: #condition to the world 3x5.
            move()
            if front_is_blocked():
                turn_left()
                turn_left()
                move()
                put_beeper()

def world_5x5_and_7x7_and_10x8():#conditions to the world Midpoint Karel, 7x7 and Midpoint 8.
    if facing_east():
        if front_is_clear():
            for c in range(2):
                move()
            if front_is_blocked():
                return_to_center()
            else:
                move()
                move()
                if front_is_blocked():#7x7.
                    return_to_center_10x8_or_7x7()
                else: #10x8.
                    move()
                    return_to_center_10x8_or_7x7()

def return_to_center():#return to the center of first row.
    turn_left()
    turn_left()
    move()
    move()
    put_beeper()

def return_to_center_10x8_or_7x7():#return to the center of first row of 10x8 world or 7x7 world.
    turn_left()
    turn_left()
    move()
    move()
    move()
    put_beeper()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
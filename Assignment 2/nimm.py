"""
File: nimm.py
-------------------------
Add your comments here.
"""


def main():
    """
    pre condition: needs to be 1 or 2.
    player option: input with pre condition after.
    player_turn: created to change the player of the game.
    20 stones in the beggining of the game.
    """
    stones = 20
    player_turn = 1
    print('There are 20 stones left')
    while stones > 0:
        player_option = int(input(f'Player {player_turn} would you like to remove 1 or 2 stones? '))
        while player_option != 1 and player_option != 2:
            player_option = int(input('Please enter 1 or 2: '))
        stones -= player_option
        if player_turn == 1:
            player_turn += 1
        else:
            player_turn = 2
            player_turn -= 1
        print()
        if stones != 0:
            print(f'There are {stones} stones left')
    if stones == 0:
        if player_turn == 1:
            print('Player 1 wins!')
        else:
            print('Player 2 wins!')






# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()

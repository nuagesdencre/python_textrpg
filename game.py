# Python Text RPG
# Created by V Savard, inspired by Bryan Tong's Tutorial

import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100


#### Player Setup ####
class player:
    def __init___(self):
        self.name = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = 'starting_zone'


myPlayer = player()


#### Title Screen ####

def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        start_game()  # placeholder until written
    elif option.lower() == ("help"):
        help.menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid command.")
        option = ("> ")
        if option.lower() == ("play"):
            start_game()  # placeholder until written
        elif option.lower() == ("help"):
            help.menu()
        elif option.lower() == ("quit"):
            sys.exit()


def title_screen():
    os.system('clear')
    print('###############################################')
    print('#         Welcome to this Text RPG!           #')
    print('###############################################')
    print(' > Play                                        ')
    print(' > Help                                        ')
    print(' > Quit                                        ')
    print(' Have fun.                                     ')
    title_screen_selections()


def help_menu():
    print('###############################################')
    print('#         Welcome to this Text RPG!           #')
    print('###############################################')
    print('- Use up, down, left and right to move.        ')
    print('- Type your commands                           ')
    print('- Use "look" to inspect something              ')
    print('- Email me if there is a bug.                  ')
    title_screen_selections()


#### Game functionality ####
def start_game():
    #### map ####
    """
    a1 a2...
    -------------
    |  |  |  |  | a4
    -------------
    |  |  |  |  | b4 ...
    -------------
    |  |  |  |  |
    -------------
    |  |  |  |  |
    -------------
    """
    ZONENAME= ''
    DESCRIPTION = 'description'
    EXAMINATION = 'examination'
    SOLVED = False
    UP = 'up', 'north'
    DOWN = 'down', 'south'
    LEFT = 'left', 'west'
    RIGHT = 'right', 'east'

    solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
                     'b1': False, 'b2': False, 'b3': False, 'b4': False,
                     'c1': False, 'c2': False, 'c3': False, 'c4': False,
                     'd1': False, 'd2': False, 'd3': False, 'd4': False}

    zonemap = {
    }
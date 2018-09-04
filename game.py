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
    print('#          Welcome to this Text RPG           #')
    print('###############################################')
    print(' > Play                                        ')
    print(' > Help                                        ')
    print(' > Quit                                        ')
    print(' Have fun.                                     ')
    title_screen_selections()


def help_menu():
    print('###############################################')
    print('#          Welcome to this Text RPG           #')
    print('###############################################')
    print('- Use up, down, left and right to move.        ')
    print('- Type your commands                           ')
    print('- Use "look" to inspect something              ')
    print('- Email me if there is a bug.                  ')
    title_screen_selections()

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


ZONENAME = ''
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
    'a1': {
        'ZONENAME': 'A1',
        'DESCRIPTION': 'description',
        'EXAMINATION': 'examination',
        'SOLVED': False,
        'UP': '',
        'DOWN': 'b1',
        'LEFT': '',
        'RIGHT': 'a2'
    },
    'a2': {
        'ZONENAME': 'A2',
        'DESCRIPTION': 'description',
        'EXAMINATION': 'examination',
        'SOLVED': False,
        'UP': '',
        'DOWN': 'b2',
        'LEFT': 'a1',
        'RIGHT': 'a3'
    },
    'a3': {
        'ZONENAME': 'A3',
        'DESCRIPTION': 'description',
        'EXAMINATION': 'examination',
        'SOLVED': False,
        'UP': '',
        'DOWN': 'b3',
        'LEFT': 'a2',
        'RIGHT': 'a4'
    },
    'a4': {
        'ZONENAME': 'A4',
        'DESCRIPTION': 'description',
        'EXAMINATION': 'examination',
        'SOLVED': False,
        'UP': '',
        'DOWN': 'b4',
        'LEFT': 'a3',
        'RIGHT': ''
    },

    'b1': {
        'ZONENAME': 'B1',
        'DESCRIPTION': 'description',
        'EXAMINATION': 'examination',
        'SOLVED': False,
        'UP': 'a1',
        'DOWN': 'c1',
        'LEFT': '',
        'RIGHT': 'b2'
    },
    'b2': {
        'ZONENAME': 'B2',
        'DESCRIPTION': 'description',
        'EXAMINATION': 'examination',
        'SOLVED': False,
        'UP': 'a2',
        'DOWN': 'c2',
        'LEFT': 'b1',
        'RIGHT': 'b3'
    },
    'b3': {
        'ZONENAME': 'B3',
        'DESCRIPTION': 'description',
        'EXAMINATION': 'examination',
        'SOLVED': False,
        'UP': 'a3',
        'DOWN': 'c3',
        'LEFT': 'b2',
        'RIGHT': 'b4'
    },
    'b4': {
        'ZONENAME': 'B4',
        'DESCRIPTION': 'description',
        'EXAMINATION': 'examination',
        'SOLVED': False,
        'UP': 'a4',
        'DOWN': 'c4',
        'LEFT': 'b3',
        'RIGHT': ''
    },

    'c1': {
        'ZONENAME': 'c1',
        'DESCRIPTION': 'description',
        'EXAMINATION': 'examination',
        'SOLVED': False,
        'UP': 'b1',
        'DOWN': 'd1',
        'LEFT': '',
        'RIGHT': 'c2'
    },
    'c2': {
        'ZONENAME': 'c2',
        'DESCRIPTION': 'description',
        'EXAMINATION': 'examination',
        'SOLVED': False,
        'UP': 'b2',
        'DOWN': 'd2',
        'LEFT': 'c1',
        'RIGHT': 'c3'
    },
    'c3': {
        'ZONENAME': 'c3',
        'DESCRIPTION': 'description',
        'EXAMINATION': 'examination',
        'SOLVED': False,
        'UP': 'b3',
        'DOWN': 'd3',
        'LEFT': 'c2',
        'RIGHT': 'c4'
    },
    'c4': {
        'ZONENAME': 'c4',
        'DESCRIPTION': 'description',
        'EXAMINATION': 'examination',
        'SOLVED': False,
        'UP': 'b4',
        'DOWN': 'd4',
        'LEFT': 'c3',
        'RIGHT': ''
    },

    'd1': {
        'ZONENAME': 'd1',
        'DESCRIPTION': 'description',
        'EXAMINATION': 'examination',
        'SOLVED': False,
        'UP': 'c1',
        'DOWN': '',
        'LEFT': '',
        'RIGHT': 'd2'
    },
    'd2': {
        'ZONENAME': 'd2',
        'DESCRIPTION': 'description',
        'EXAMINATION': 'examination',
        'SOLVED': False,
        'UP': 'c2',
        'DOWN': '',
        'LEFT': 'd1',
        'RIGHT': 'd3'
    },
    'd3': {
        'ZONENAME': 'd3',
        'DESCRIPTION': 'description',
        'EXAMINATION': 'examination',
        'SOLVED': False,
        'UP': 'c3',
        'DOWN': '',
        'LEFT': 'd2',
        'RIGHT': 'd4'
    },
    'd4': {
        'ZONENAME': 'd4',
        'DESCRIPTION': 'description',
        'EXAMINATION': 'examination',
        'SOLVED': False,
        'UP': 'c4',
        'DOWN': '',
        'LEFT': 'd3',
        'RIGHT': ''
    },
}


#### Game interactivity ####

def print_location():
    print('\n' + ('#' * (4 + (len(myPlayer.location)))))
    print('# ' + myPlayer.location + ' #')
    print('# ' + zonemap[myPlayer.position]['DESCRIPTION'] + ' #')
    print('\n' + ('#' * (4 + (len(myPlayer.location)))))


def prompt():
    print('\n' + '=========================')
    print('what would you like to do?')
    action = input("> ")
    acceptable_actions = ['move', 'go', 'travel',
                          'walk', 'quit', 'examine',
                          'interact', 'look', 'inspect']
    while action.lower() not in acceptable_actions:
        print("Unknown action, try again!")
        action = input("> ")
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        player_move(action.lower())
    elif action.lower() in ['examine', 'interact', 'look', 'inspect']:
        player_examine(action.lower())


def player_move(myAction):
    ask = 'Where do you want to go exactly?\n'
    dest = input(ask)
    if dest in ['up', 'north']:
        destination = zonemap[myPlayer.location]['UP']
        mouvement_handler(destination)
    elif dest in ['left', 'west']:
    elif dest in ['right', 'east']:
    elif dest in ['down', 'south']:


def mouvement_handler(destination):
    print('\n' + 'You have arrived to your destination (' + destination + ').')
    myPlayer.location = destination
    print_location()


def player_examine(action):
    if zonemap[myPlayer.location]['SOLVED']
        print('You have already been to this zone.')
    else:
        print('You can trigger a puzzle here.')

    #### Game functionality ####


def start_game():
    return

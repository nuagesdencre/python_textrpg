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


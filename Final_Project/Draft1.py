import random
import time

class weapon:
    def __init__(self, damage, name,):
        self.damage = damage
        self.name = name
    def weapon_attack(self):
        print('You swing your', self.name)
class player:
    def __init__(self, name,):
        self.name = name
    
sword = weapon(15, 'sword')
inventory = []

player = input('Welcome new employee of Starfax corp. Please enter your name: ')
profession = input('What is your area of expertise? Engineer or security?')
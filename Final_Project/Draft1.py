import random
import time

class weapon:
    def __init__(self, damage, name,):
        self.damage = damage
        self.name = name
    def weapon_attack(self):
        print('You swing your', self.name)
class player:
    def __init__(self, name, health):
        self.name = name
        self.health = health

def user_att(attacker, defender):

sword = weapon(15, 'sword')
alien_health = 100
user_health = 0

# Opening of game. Before main loop
print('Welcome to Alien Fight! Thank you for choosing to play this game.')
while True:
    difficulty = input('Please select diffulculty. [H]ard, [M]edium, or [E]easy. ')
    print(difficulty)
    if difficulty == 'H':
        user_health = 75
        break
    if difficulty == 'M':
        user_health = 100
        break
    if difficulty =='E':
        user_health = 125
        break
    else:
        print('Invalid answer')
print(user_health)
user = player('', user_health)
user.name = input('Welcome new employee of Starfax corp. Please enter your name: ')
print('Welcome engineer', user.name +'''. There is a disturbance on sublevel 3. An
atmospheric breach has been detected. You have been tasked with sealing the breach and investigating
it's cause. Please proceed immediately.''')
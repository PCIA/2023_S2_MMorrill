import random
import time

class user:
    def __init__(self, name, health):
        self.name = name
        self.health = health

def hit_check(attacker_number, defender_number):
    if attacker_number == defender_number:
        return True
    else:
        return False

def alien_attack():
    global player_health
    attacker_choice = random.randint(0,2)
    defender_choice = 0
    damage = 0
    alien_texts = [['The alien roars and lunges toward you!', 'Fail! It bites into your flesh'],
                   ['You hear a growl, its going to spit acid!', 'Fail! Acid sears your skin'],
                   ['The alien swings its claw toward you!', 'Fail! The claw slahes you']]
    alien_text_choice = random.randint(0,2)
    print(alien_texts[alien_text_choice][0])
    x = 0
    while x == 0:
        defender_choice = int(input('What do you do?\n(1)Dodge left\n(2) Dodge right\n(3) Jump back\n'))
        defender_choice = defender_choice - 1
        if defender_choice >= 0 and defender_choice <=2:
            hit = hit_check(attacker_choice, defender_choice)
            x = 1
        else: 
            print('Invalid answer. Please enter number between 1 and 3')
    if hit == True:
        print(alien_texts[alien_text_choice][1])
        player_health = player_health - 20
        print('Your health is now',player_health)
    else:
        print('Success! You dodged the attack')
    
alien_health = 100
player_health = 0

# Opening of game. Before main loop
print('Welcome to Alien Fight! Thank you for choosing to play this game.')
while True:
    difficulty = input('Please select diffulculty. [H]ard, [M]edium, or [E]easy. ')
    print(difficulty)
    if difficulty == 'H':
        player_health = 75
        break
    if difficulty == 'M':
        player_health = 100
        break
    if difficulty =='E':
        player_health = 125
        break
    else:
        print('Invalid answer')
print(player_health)
player = user('', player_health)
player.name = input('Welcome new employee of Starfax corp. Please enter your name: ')
print('Welcome seargant', player.name +'''. There is a disturbance on sublevel 3. An
atmospheric breach has been detected. You have been tasked with sealing the breach and investigating
it's cause. Please proceed immediately.''')

while player_health > 0:
    turn = 0
    if turn == 0:
        alien_attack()
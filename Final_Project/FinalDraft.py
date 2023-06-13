import random
import time

class entity:
    def __init__(self, name, health):
        self.name = name
        self.health = health

def slow_text(text):
    for i in text:
        time.sleep(0.05)
        print(i, end='', flush = True)

def hit_check(attacker_number, defender_number):
    if attacker_number == defender_number:
        return True
    else:
        return False

def alien_attack():
    attacker_choice = random.randint(0,2)
    defender_choice = 0
    alien_texts = [['The alien roars and lunges toward you!', 'Fail! It bites into your flesh'],
                   ['You hear a growl, its going to spit acid!', 'Fail! Acid sears your skin'],
                   ['The alien swings its claw toward you!', 'Fail! The claw slahes you']]
    alien_text_choice = random.randint(0,2)
    print(alien_texts[alien_text_choice][0])

    time.sleep(1)

    while True:
        time.sleep(1)
        defender_choice = int(input('What do you do?\n(1)Dodge left\n(2)Dodge right\n(3)Jump back\n'))
        defender_choice = defender_choice - 1
        if defender_choice >= 0 and defender_choice <=2:
            hit = hit_check(attacker_choice, defender_choice)
            break
        else: 
            print('Invalid answer. Please enter number between 1 and 3')
    if hit == True:
        print(alien_texts[alien_text_choice][1])
        player.health = player.health - 10
        print('Your health is now',player.health)
    else:
        print('Success! You dodged the attack')

def player_attack():

    attacker_choice = 0
    defender_choice = random.randint(0,2)
    print('You have a chance to attack!')

    while True:
        time.sleep(1)
        print('What do you do?')
        attacker_choice = int(input('\n(1)Swing left\n(2)Swing right\n(3)Swing forward\n'))
        attacker_choice = attacker_choice - 1
        if attacker_choice >= 0 and attacker_choice <=2:
            hit = hit_check(attacker_choice, defender_choice)
            break
        else: 
            print('Invalid answer. Please enter number between 1 and 3')
    if hit == True:
        time.sleep(1)
        print('Success! You hit the alien. It howls in pain.')
        alien.health = alien.health - 10
        time.sleep(1)
        print('The alien now has a health of',alien.health)
    else:
        print('Fail! The alien dodged the attack')

    
first_time = True
player_play = True
EASY_DIFFICULTY_HEALTH = 100
MEDIUM_DIFFICULTY_HEALTH = 50
HARD_DIFFICULTY_HEALTH = 30

while player_play:

    if first_time:
        while True:
            print('Welcome to Alien Fight! Would you like to play?.')
            player_choice = input('[Y]es or [N]o ').upper()[0]
            if player_choice == 'N':
                player_play = False
                break
            elif player_choice == 'Y':
                break
            else:
                print('Invalid input')

    if player_play == False:
        break

    player = entity('', 0)
    alien = entity('alien', 50)

    while True:
        time.sleep(0.25)
        difficulty = input('Please select diffulculty. [H]ard, [M]edium, or [E]easy. ').upper()[0]
        if difficulty == 'H':
            player.health = HARD_DIFFICULTY_HEALTH
            break
        if difficulty == 'M':
            player.health = MEDIUM_DIFFICULTY_HEALTH
            break
        if difficulty =='E':
            player.health = EASY_DIFFICULTY_HEALTH
            break
        else:
            print('Invalid answer')

    entrytext1 = 'Welcome new employee of Starfax corp. Please enter your name: '
    entrytext2 = 'Welcome marine' + player.name + '''. There is a disturbance on sublevel 3. An
atmospheric breach has been detected. You have been tasked with sealing the breach and investigating
it's cause. Please proceed immediately.'''

# The following code loops came from chatGPT after giving it the code and the prompt
# 'Hey I have this code. I'm trying to print some text out by individally having the letters 
# typed on screen, except it creates a new line for every letter and I don't want that.
#  How do I fix it?'
    for i in entrytext1:
        time.sleep(0.05)
        print(i, end='', flush = True)
    player.name = input('')
    for i in entrytext2:
        time.sleep(0.05)
        print(i, end='', flush = True)

    time.sleep(2)

    print("\nYou begin descending into the lower levels of the ship.")
    print("Lights flicker as you enter the corridor. You hear scratching.")
    print("BOOM!")
    print("The door slams behind you. You try to open it but it's stuck.")
    print("A shape emerges from the darkness. An alien. It has infested the ship.")
    print("You know in order to save the ship you have to kill it. The aliens growls")
    print("You pick up a piece of broken pipe and preapre to fight it.")
    turn = 0
    while player.health > 0:
        if turn == 0:
            player_attack()
            turn = 1
        elif turn == 1:
            alien_attack()
            turn = 0
    if player.health <= 0:
        time.sleep(1)
        print('Defeat. The alien has killed you. Rest well marine.')
    else:
        time.sleep(1)
        print('''The alien gives a final roar before collapsing down. Well done marine, you'll get
a medal for this.''')
    closingtext1 = 'Would you like to try again?'

    for i in closingtext1:
        time.sleep (0.05)
        print(i, end='', flush = True)

    while True:
        response = input('[Y]es or [N]o ').upper()[0]
        if response == 'N':
            player_play = False
            break
        elif response == 'Y':
            player_play = True
            break
        else:
            print('Invalid response')
    first_time = False
        
print('Thank you for playing!')
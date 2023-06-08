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
    alien_texts = [['The alien roars and lunges toward you!', 'Fail! It bites into your flesh'],
                   ['You hear a growl, its going to spit acid!', 'Fail! Acid sears your skin'],
                   ['The alien swings its claw toward you!', 'Fail! The claw slahes you']]
    alien_text_choice = random.randint(0,2)
    time.sleep(1.5)
    print(alien_texts[alien_text_choice][0])
    x = 0
    while x == 0:
        time.sleep(1)
        defender_choice = int(input('What do you do?\n(1)Dodge left\n(2)Dodge right\n(3)Jump back\n'))
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

def player_attack():
    global alien_health
    attacker_choice = 0
    defender_choice = random.randint(0,2)
    print('You have a chance to attack!')

    while True:
        time.sleep(1)
        attacker_choice = int(input('What do you do?\n(1)Swing left\n(2)Swing right\n(3)Swing forward\n'))
        attacker_choice = attacker_choice - 1
        if attacker_choice >= 0 and attacker_choice <=2:
            hit = hit_check(attacker_choice, defender_choice)
            break
        else: 
            print('Invalid answer. Please enter number between 1 and 3')
    if hit == True:
        time.sleep(1)
        print('Success! You hit the alien. It howls in pain.')
        alien_health = alien_health - 20
        time.sleep(1)
        print('The alien now has a health of',alien_health)
    else:
        print('Fail! The alien dodged the attack')

    
alien_health = 50
player_health = 0
first_time = True
player_play = True

while player_play == True:
    if first_time == True:
        while True:
            print('Welcome to Alien Fight! Would you like to play?.')
            player_choice = input('[Y]es or [N]o ')
            if player_choice == 'N':
                player_play = False
                break
            elif player_choice == 'Y':
                looping1 = False
            else:
                print('Invalid input')
    if player_play == False:
        break
    while True:
        time.sleep(0.25)
        difficulty = input('Please select diffulculty. [H]ard, [M]edium, or [E]easy. ')
        if difficulty == 'H':
            player_health = 25
            break
        if difficulty == 'M':
            player_health = 50
            break
        if difficulty =='E':
            player_health = 100
            break
        else:
            print('Invalid answer')
    player = user('', player_health)

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
    time.sleep(3)

    print('''You begin descending into the lower levels of the ship. Lights flicker as you enter
the corridor. You hear scratching. BOOM! The door slams behind you. A shape emerges from the darkness.
An alien has infested the ship. You try to open the door but it's stuck. You have to kill it to
save the ship. The alien growls as you pick up a broken pipe.''')

    while player_health > 0:
        turn = 0
        if turn == 0:
            player_attack()
            turn = 1
        elif turn == 1:
            alien_attack()
            turn = 0
    if player_health <= 0:
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
        response = input('[Y]es or [N]o ')
        if response == 'N':
            player_play = False
            break
        elif response == 'Y':
            player_play = True
            break
        else:
            print('Invalid response')
        
print('Thank you for playing!')
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
    time.sleep(2)
    print(alien_texts[alien_text_choice][0])

    time.sleep(1)

    while True:
        time.sleep(2)
        defender_choice = int(input('What do you do?\n(1)Dodge left\n(2)Dodge right\n(3)Jump back\n'))
        if defender_choice >= 0 and defender_choice <=2:
            defender_choice = defender_choice - 1
            hit = hit_check(attacker_choice, defender_choice)
            break
        else: 
            print('Invalid answer. Please enter number between 1 and 3')
    if hit == True:
        time.sleep(2)
        print(alien_texts[alien_text_choice][1])
        player.health = player.health - 10
        print('Your health is now',player.health)
    else:
        time.sleep(2)
        print('Success! You dodged the attack')

def player_attack():

    attacker_choice = 0
    defender_choice = random.randint(0,2)

    time.sleep(2)
    print('You have a chance to attack!')

    while True:
        time.sleep(2)
        print('What do you do?')
        time.sleep(1)
        attacker_choice = int(input('\n(1)Swing left\n(2)Swing right\n(3)Swing forward\n'))
        if attacker_choice >= 0 and attacker_choice <=2:
            attacker_choice = attacker_choice - 1
            hit = hit_check(attacker_choice, defender_choice)
            break
        else: 
            print('Invalid answer. Please enter number between 1 and 3')

    time.sleep(2)

    if hit == True:
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
            slow_text('Welcome to Alien Fight! Would you like to play?.')
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
        time.sleep(1)
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

    slow_text('Welcome new employee of Starfax corp. Please enter your name: ')
    player.name = input('')
    slow_text('Welcome marine ' + player.name + '''. There is a disturbance on sublevel 3. An
atmospheric breach has been detected. You have been tasked with sealing the breach and investigating
it's cause. Please proceed immediately.''')

    time.sleep(2)

    print("\nYou begin descending into the lower levels of the ship.")
    time.sleep(3)
    print("Lights flicker as you enter the corridor. You hear scratching.")
    time.sleep(3)
    print("BOOM!")
    time.sleep(1)
    print("The door slams behind you. You try to open it but it's stuck.")
    time.sleep(3)
    print("A shape emerges from the darkness. An alien. It has infested the ship.")
    time.sleep(3)
    print("You know in order to save the ship you have to kill it. The aliens growls")
    time.sleep(2)
    print("You pick up a piece of broken pipe and prepare to fight it.")

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
        
    slow_text('Would you like to try again?')

    while True:
        response = input('[Y]es or [N]o ').upper()[0]
        if response == 'N':
            player_play = False
            break
        elif response == 'Y':
            break
        else:
            print('Invalid response')
    first_time = False
        
slow_text('Thank you for playing!')
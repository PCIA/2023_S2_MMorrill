attacker_choice = 0
while attacker_choice == 0:
    print('The alien swings its claw toward you!')
    defender_choice = input('''What do you do? 
(0) Dodge left
(1) Dodge right
(2) Jump back ''')
    if defender_choice == 0 or defender_choice == 1 or defender_choice == 2:
        print('success')
        attacker_choice = 5
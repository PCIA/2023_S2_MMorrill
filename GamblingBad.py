import time
import random
PlayerMoney = 0
print("'Hey Kids! Today we'll be learning about why gambling is bad.'")
time.sleep(1.25)
answer = input("Are you ready? [Yes or No] ")
if answer == "Yes": print("'Good. Let us begin.'")
if answer == "No": print("'Too bad! We're starting.'")
time.sleep(1.25)
print("*you walk towards a slot machine*")
time.sleep(1.25)
print("'Alright, now spin the machine.'")
time.sleep(1.25)
choice1 = input("Do you spin the machine? [Yes or No] ")
if choice1 == "Yes": print('*The machine rumbles and spins*')
else: print('*The instructor pulls the lever for you*')
slotvalue = ("Cherry","7","King","Queen","Diamond")
slot1 = random.choice(slotvalue)
slot2 = random.choice(slotvalue)
slot3 = random.choice(slotvalue)
time.sleep(2)
print("You got", slot1, slot2, "and", slot3)
if slot1 == slot2 or slot3: 
    print("Congratulations you've won 10 coins!")
    PlayerMoney = PlayerMoney + 10
time.sleep(1.25)
print("You now have", PlayerMoney,"Gold Coins")
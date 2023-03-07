import random
import time
winner = ""
random_choice = random.randint(0,2)
if random_choice == 0:
    computer_choice = "Rock"
elif random_choice == 1:
    computer_choice = "Paper"
else:
    computer_choice = "Scissors"
user_choice = ""
while (user_choice != "Rock" and
    user_choice != "Paper" and
    user_choice != "Scissors"):
    user_choice = input("Rock, Paper, or Scissors? ")
print("You chose,",user_choice,"and the computer chose",computer_choice)
user_choice = (user_choice).upper()
computer_choice = (computer_choice).upper()
if computer_choice == user_choice:
    winner = "Tie"
if computer_choice == "ROCK" and user_choice == "SCISSORS":
    winner = "Computer"
if computer_choice == "PAPER" and user_choice == "ROCK":
    winner = "Computer"
if computer_choice == "SCISSORS" and user_choice == "PAPER":
    winner = "Computer"
else:
    winner = "User"
if winner == "Tie":
    time.sleep(1.25)
    print("We both chose",computer_choice,"so its a draw.")
else: 
    time.sleep(1.25)
    print("The",winner,"wins!")
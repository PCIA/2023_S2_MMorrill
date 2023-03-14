import time
import random
dictionary = ["house","car","sun","fan","bookshelf","gemstone"]
word = random.choice(dictionary)
wrongchoices = ''
userWrong = 0
hidden_word = '_'*len(word)
gamestate0 =(
' +----|\n'
'      |\n'
'      |\n'
'     ===')
gamestate1 =(
' +----|\n'
' O    |\n'
'      |\n'
'     ===')
gamestate2 =(
' +----|\n'
' O    |\n'
' |    |\n'
'     ===')
gamestate3 =(
' +----|\n'
' O    |\n'
'/|    |\n'
'     ===')
gamestate4 =(
' +----|\n'
' O    |\n'
'/|\   |\n'
'     ===')
gamestate5 =(
' +----|\n'
' O    |\n'
'/|\   |\n'
'/    ===')
gamestate6 =(
' +----|\n'
' O    |\n'
'/|\   |\n'
'/ \  ===')
gamestatewin =(
' O --(Yippee! Thanks hero)  \n'
'/|\   \n'
'/ \  ')
gamestate = gamestate0
checkgame = 0
print(gamestate)
print('Please hero! We need you to save little Timmy!')
while '_' in hidden_word and userWrong<6:
    def checkstate():
        global checkgame 
        global gamestate 
        if checkgame == 0:gamestate = gamestate0
        if checkgame == 1:gamestate = gamestate1
        if checkgame == 2:gamestate = gamestate2
        if checkgame == 3:gamestate = gamestate3
        if checkgame == 4:gamestate = gamestate4
        if checkgame == 5:gamestate = gamestate5
        if checkgame == 6:gamestate = gamestate6
    if userWrong == 5: print("Careful! If you guess wrong a small child dies...")
    print(' '.join(hidden_word))
    guess = input("Guess a letter: ").lower()
    if len(guess) > 1:
        time.sleep(0.75)
        print('Please only one letter at a time.')
    elif guess in wrongchoices:
        print(gamestate)
        time.sleep(0.75)
        print("You already guessed that letter! You silly goose, try again.")
    elif guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                hidden_word = hidden_word[:i] + guess + hidden_word[i+1:]
        if hidden_word != word:
            print(gamestate)
            time.sleep(0.75)
            print("Correct! Lets see if you can keep it up. For Timmy's sake.")
    elif guess not in word:
        userWrong = userWrong + 1
        checkgame = checkgame + 1
        checkstate()
        if userWrong < 6:
            print(gamestate)
            print('Bad guess! Little Timmy is one step closer to death.')
if hidden_word == word:
    gamestate = gamestatewin
    print(gamestate)
    time.sleep(2)
    print('Good job! Little Timmy lives to see another day')
else: 
    print (gamestate)
    time.sleep(1)
    print('You have failed. Little timmy is lost. You will carry this to your grave you monster.')
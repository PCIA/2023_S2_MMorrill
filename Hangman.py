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
gamestate = gamestate0
while '_' in hidden_word and userWrong>6:
    print(gamestate)
    guess = input("So far the word is,",hidden_word,"Guess a letter: ").lower()
    if len(guess) > 1:
        print('Please only one letter at a time.')
    elif guess in wrongchoices:
        print("You already guessed that letter! You silly goose, try again.")
    elif guess in word:
        for i in len(word):
            if word[i] == guess:
                hidden_word[i] = guess
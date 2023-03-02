import random
wordDictionary = ["house","car","sun","fan","bookshelf","gemstone"]
wordChoice = random.choice(wordDictionary)
userWrong = 0
display = "_" * len(wordChoice)

if userWrong == 0:
    print("+----|")
    print("     |")
    print("     |")
    print("     |")
    print("    === The word is",display)
if userWrong == 1:
    print("+----|")
    print("O    |")
    print("     |")
    print("     |")
    print("    ===")
elif userWrong == 2:
    print("+----|")
    print("O    |")
    print("|   |")
    print("    |")
    print("    ===")
elif userWrong == 3:
    print(" +----|")
    print(" O    |")
    print(" |    |")
    print("/      |")
    print("    ===")
elif userWrong == 4:
    print(" +----|")
    print(" O    |")
    print(" |   |")
    print("/ \   |")
    print("    ===")
elif userWrong == 5:
    print(" +----|")
    print(" O    |")
    print("/|   |")
    print("/ \   |")
    print("    ===")
if userWrong == 6:
    print(" +----|")
    print(" O    |")
    print("/|\   |")
    print("/ \   |")
    print("    ===")
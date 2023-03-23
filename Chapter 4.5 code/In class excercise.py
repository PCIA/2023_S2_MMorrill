sentence = input('Make a sentence please: ')
words = sentence.split()
syllables = []
for word in words:
    index=words.index(word)
    syllablecount = 0
    for char in word: 
        if char in "aeiouAEIOU":
            syllablecount = syllablecount + 1
        syllables.append(syllablecount)
print(word + ' ') + str(syllables[index])


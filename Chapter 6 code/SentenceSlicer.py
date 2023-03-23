text = """I really love apples. The thing is I also like oranges. But how do I know? Well I 
eat them of course! So really the key is just trying new things and finding what you like and dont
like!"""
def count_sentences(text):
    count = 0
    for char in (text):
        if char in '!.?':
            count = count + 1
    return count
def count_syllables_in_word(word):
    count = 0
    if len(word) <= 3:
        return 1
    vowels = 'aeiouAEIOU'
    prev_char_was_vowel = False
    for char in word:
        if char in 'vowels':
            if not prev_char_was_vowel:
                count = count+1
            prev_char_was_vowel = True
        else:
            prev_char_was_vowel = False
    return count
def count_syllables(text):
    count = 0
    words = text.split()
    for word in words:
        # word_count represents num of syllables
        word_count = count_syllables_in_word(word)
        count = count + word_count
    return count
def compute_readability (text):
    words = text.split()
    total_words = len(words)
    total_sentences = count_sentences(text)
    total_syllables = count_syllables(text)
    print(total_words)
    print(total_sentences)
    print(total_syllables)
compute_readability(text)



    

def getSentenceCount(text_to_analyze):
    count = 0
    words = text_to_analyze.split
    for word in words:
        i = 0
        while i <= len(word):
            character = word[i]
            if character in ".?!":
                count = count + 1
            i = i + 1

    return count


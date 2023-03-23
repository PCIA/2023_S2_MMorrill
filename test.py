theText = 'I really love apples. I also love cherries! But do I like oranges?'
def countSentences(theText):
   sentenceCount = 0
   
   for char in theText:
      if char == '.' or '!' or '?':
         sentenceCount = sentenceCount + 1

   return sentenceCount
answer = countSentences(theText)
print(answer)

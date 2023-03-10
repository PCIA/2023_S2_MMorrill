import random
smoothies = ["Stawberry","Mango","Black Death"]
order = random.choice(smoothies)
print(order)
length = len(smoothies)
print(length)
characters = ['t',"a",'c','o']
output = ''
length = len(characters)
i = 0
while (i<length):
    output = output + characters[i]
    i = i+1 
length = length * -1
i = -2
while (i>=length):
    output = output + characters[i]
    i = i - 1
print(output)


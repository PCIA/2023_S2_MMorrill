import time
coolwords = ['Big',"Hairy",'Tiny','Intelligent']
animals = ['Dog', 'Gorilla','Cat','Owl']
length = len(animals)
i = 0
while (i<length):
    outputword = animals[i]
    p = 0
    while (p<length):
        time.sleep(0.75)
        print(coolwords[p],outputword)
        p = p + 1
    i = i+1






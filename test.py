import time
def cycle_list(list):
    for i in list:
        time.sleep(1)
        print(i)
test = ['Run','Hide','Eua']
cycle_list(test)
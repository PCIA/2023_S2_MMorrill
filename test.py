import time
entrytext1 = 'Welcome new employee of Starfax corp. Please enter your name: '

for i in entrytext1:
    time.sleep(0.05)
    print(i, end='', flush=True)

player = input('')

entrytext2 = 'Welcome marine ' + player + '''. There is a disturbance on sublevel 3. An
atmospheric breach has been detected. You have been tasked with sealing the breach and investigating
it's cause. Please proceed immediately.'''

for i in entrytext2:
    time.sleep(0.05)
    print(i, end='', flush=True)
time.sleep(3)

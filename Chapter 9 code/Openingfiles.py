my_file = input('Enter a file path:'),
try:
    text = open(my_file,'r')
    read = text.read()
    print(read)
except:
    print('File not found')
finally:
    print('Thank you for trying our system')
    my_file.close

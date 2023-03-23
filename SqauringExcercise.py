def exponent (integer, power):
    return integer ** power
def square_number (number):
    squarednumber = exponent(int(number),2)
    return squarednumber
while True:
    number = input('Please enter a number, or press q to quit. ')
    if number == 'q':
        break
    try:
        print('The square of your number is', square_number(number))
    except ValueError:
        print("Invalid entry. Please try again.")



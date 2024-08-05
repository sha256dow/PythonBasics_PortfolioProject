# To Git:

# Imports:
import random
import string
import time

# Function:
  # Setting lenght and bools:
def passwordGenerator(lenght=8, includeDigits=True, includeSymbols=True):
    characters = string.ascii_letters 
    if includeDigits:
        characters = characters + string.digits#
    if includeSymbols:
        characters = characters + string.punctuation#
    
    passwd = ''.join(random.choice(characters) for _ in range(lenght))
    return print(f'Your Secure Password with lenght=8 is:', passwd)

def mainFunction():
    print('Generating random secure password...')
    time.sleep(0.5)
    print('Your Secure Password will be generated above.')
    time.sleep(2)
    return passwordGenerator()
    
if __name__ == '__main__':
    mainFunction()

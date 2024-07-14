print("Is it a Palindrome? Let's check! Please enter the word you want to check...")

class Palindrome:
    def __init__(self) -> None:
        pass
        
    def isItAPalindrome(): # Is it a palindrome? LOL
        word = input('Word: ').upper()
        #word = word[::-1]

        if word == word[::-1]:
            print('Palindrome')
        else:
            print(f'{word} is NOT a palindrome.')
    

    isItAPalindrome() # returns

    

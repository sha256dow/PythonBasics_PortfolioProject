print("Is it a Palindrome? Let's check! Please enter the word you want to check...")

def isItAPalindrome(): # Is it a palindrome? LOL
    word = input('Word: ').upper()
    word = word[::-1]

    if word == word[::-1]:
        print('Palindrome')
    else:
        print('Not a palindrome')
    
if __name__ == '__main__':
    isItAPalindrome() # returns

# Creating a very simple program to translate ENG words to PTBR (user input text): 

# Importing Google Translator package: 
from googletrans import Translator

def translate_to_portuguese(text: str):
    translator = Translator()
    translated_text = translator.translate(text, src='auto', dest='pt').text
    return translated_text

if __name__ == "__main__":
    user_input = input("Text to translate: ")
    translated_text = translate_to_portuguese(user_input)
    print("Texto traduzido para Português-BR: ")
    print(translated_text)


# PALINDROME
# This program verify if the word typed from the user is palindrome or not.
# Author: Marcelo Magario 03/09/2022

word = str(input('Enter your word: ')).upper()
word_reversed = word[::-1].upper()
print(f'Your word: {word}')
print(f'Your backwards: {word_reversed}')
print(f"It's Palindrome" if word == word_reversed else "It's NOT Palindrome")


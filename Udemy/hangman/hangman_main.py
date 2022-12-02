"""
HangMam Game
"""
import random
import copy
import hangman_art
import hangman_words
print(hangman_art.logo)

'''*************************************************************************************'''
stages = hangman_art.stages
lives = 6

#Choosing a random letter. So for convinence we will just take a list containing 3 words
word_list = hangman_words.word_list
choosen_word = random.choice(word_list)

#Creating a list which will show how many letter words a there and will get replaced by the letter if gusse is correct
display = ["_" for i in range(len(choosen_word))]
print(display)
'''*************************************************************************************'''

number_of_blanks = len(display)

while(number_of_blanks > 0 and lives > 0):
    display1 = copy.copy(display)
    #Asking user for input
    gusse_letter = input("Gusse a letter: ")
    a = 0
    for letter in choosen_word:
        if letter == gusse_letter:
            display[a] = gusse_letter
            number_of_blanks -= 1
        a += 1
    print(display)
    if display == display1:
        print(stages[lives])
        lives -= 1

if number_of_blanks == 0:
    print("You won")
else:
    print(stages[lives])
    print("You Lost")
    print(f"Word was {choosen_word}")
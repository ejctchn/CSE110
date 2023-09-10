"""
    1 - I added the ability for the user to enter either upper or lowercase
    2 - I added a play again feature
"""

import random

#list of words to choose from
words = ["temple", "savior", "church", "oil", "friend", "prophet", "saint", "chapel", "jesus", "christ", 
         "way", "light", "atonement", "blood", "sacrament", "water", "bread", "bishop", "counselor", "child"]
keep_playing = True

print("\nWelcome to the Word Guessing Game!")
print("All the words are religion based.")
print("If you guess a letter in the correct place, it will show as an upper case letter.")
print("If you guess a correct letter in the wrong place, it will show as a lower case letter")

while(keep_playing):
    #create the random index for the word
    rand_num = random.randint(0, (len(words)-1))
    #choose a random word
    rand_word = words[rand_num]
    placeholder = ''
    blanks = []
    for letters in rand_word:
        blanks.append("_ ")

    def find_letter(guess, rand_word, blanks):
        for letter in rand_word:
            i = 0
            for guess_letter in guess:
                if(letter == guess_letter):
                    if(guess_letter == rand_word[i]):
                        blanks[i] = guess_letter.upper() + " "
                    else:
                        blanks[i] = guess_letter.lower() + " "
                else:
                    pass
                i += 1


    print(f'\nYour hint is: {placeholder.join(blanks)} ({len(blanks)} letters)')
    guess = input("What is your guess? ").lower()
    count = 1

    while(guess != rand_word):
        if(len(guess) != len(rand_word)):
            print("Sorry, the guess must have the same number of letters as the secret word.")
        else:
            blanks = []
            for letters in rand_word:
                blanks.append("_ ")
            find_letter(guess, rand_word, blanks)
            print(f'Your hint is: {placeholder.join(blanks)} ({len(blanks)} letters)')
            count += 1
        guess = input("What is your guess? ").lower()
    print("You got it!")
    print(f'It took you {count} tries.')
    keep_asking = True
    while(keep_asking):
        keep_going = input("Do you want to keep playing (yes/no)? ")
        if(keep_going.lower() == "yes"):
            keep_asking = False
        elif(keep_going.lower() == "no"):
            keep_asking = False
            keep_playing = False
        else:
            print("Please enter a valid command.")
print("\nThanks for playing!!")
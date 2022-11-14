from random import choice
from time import time # time module

print('''



░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ████████╗░█████╗░
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ╚══██╔══╝██╔══██╗
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ░░░██║░░░██║░░██║
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░░░██║░░░██║░░██║
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ░░░██║░░░╚█████╔╝
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░

██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗  ██████╗░░█████╗░██████╗░██████╗░██╗██╗
██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║  ╚════██╗██╔══██╗╚════██╗╚════██╗██║██║
███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║  ░░███╔═╝██║░░██║░░███╔═╝░░███╔═╝██║██║
██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║  ██╔══╝░░██║░░██║██╔══╝░░██╔══╝░░╚═╝╚═╝
██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║  ███████╗╚█████╔╝███████╗███████╗██╗██╗
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝  ╚══════╝░╚════╝░╚══════╝╚══════╝╚═╝╚═╝

''')

name = input("What is your name? ")
print(f"Good Luck, {name}!")

words = ['rainbow', 'computer', 'science', 'programming',
    'python', 'mathematics', 'player', 'condition',
    'reverse', 'water', 'board', 'geeks']

word = choice(words)

figure = [
    "   ++---------+",
    "   ||         |",
    "   ||         |",
    "   ||         |",
    "   ||         |",
    "   ||         |",
    "   ||         |",
    "   ||         O",
    "   ||        /|\\",
    "   ||        / \\" ,
    "   ||            ",
    " ================"
]

print("Guess the Word: ")

guessed_word = '_' * len(word) # initialize blank letters of word


guesses = '' # holds the guesses of the player
turns = 12

start = time() # gets the starting time
limit = 30

failed = 0 # number of wrong guesses
current = 0 # initialize current time

while turns > 0:
    current = time() # gets the current time
    
    if current - start > limit: # current - start is the duration of the game
        print("Your 30 seconds is up! \n" + \
            "You Lose.\n" + \
            f"The word is: {word}" + \
              "Try again next life!!!\n" + \
            'Time Taken: 30.00 seconds'
        )
        break

    print(f"Guessed Word: {guessed_word}") # updates the guessed letters of the word
    guess = input("Guess a character: ")
    guesses += guess
 
    for char in word:
        if char in guesses:
            guessed_word = list(guessed_word) # convert to list temporarily to be mutable since string is immutable
            for i, letter in enumerate(word): # get the index and letters of the word
                if letter == char:
                    guessed_word[i] = letter # replaces _ with the guessed letter
            
    if guess not in word:
        failed += 1
        turns -= 1
        print("Wrong." + \
            f"You have {turns} more guesses.")

        for i in range(failed): # print the figure corresponding to no. of failed guesses
            print(figure[i])
            
        if turns == 0:
            print("You Lose.\n" + \
                f"The word is: {word}\n" + \
                "Try again next life!!!" + \
                f'Time Taken: {current - start} seconds\n\n')

    guessed_word = "".join(guessed_word) # convert list back to string
    if word == guessed_word:
        print("You Win\n" + \
            f"The word is: {word}" + \
            f'Time Taken: {current - start} seconds\n\n')
        break

    print("\n\n")



        
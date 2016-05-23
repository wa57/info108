#####################################################################################
# Guess My Number
#
# mpk
# mpk
# mpk
# mpk
#WRITE DOCUMENTATION
import os
import random

def guessMyNumber():

    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #mpk Build a variable to hold the score
    guessMyNumberTotal = 0

    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    os.system('cls||clear')
    print()

    print("\t\tWelcome to 'Guess My Number'!")
    print()
    print(' '*10,"I'm thinking of a number between 1 and 100.")
    print(' '*10, "Try to guess it in as few attempts as possible.\n")

    #mpk
    the_number = random.randint(1, 100)

    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #mpk Read in and validate the user's guess
    strGuess = input(' '*11 + 'Take a guess: ')
    while not strGuess.isdigit():
        strGuess = input(' '*11+'Your guess must be a number: ')
    guess = int(strGuess)
    tries = 1

    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #mpk guessing loop
    while guess != the_number:
        if guess > the_number:
            print(' '*11+'Lower...')
        else:
            print(' '*11+'Higher...')
        strGuess = input(' '*11+'Take a guess: ')
        while not strGuess.isdigit():
            strGuess = input(' '*11+'Your guess must be a number: ')
        guess = int(strGuess)
        tries += 1







    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #mpk Player scores if they guess the number with 3 or fewer tries
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    #mpk
    print()
    print(' '*12+'You guessed it! The number was', the_number)
    print(' '*12+'And it only took you', tries, 'tries!')
    if tries <= 3:
        print(' '*12+'Congratulations! You earned a point.')
        guessMyNumberTotal += 1
    else:
        print(' '*12+"Unfortunately, you didn't earn a point this time")




    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #mpk Return the score to GameWorld
    return guessMyNumberTotal

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

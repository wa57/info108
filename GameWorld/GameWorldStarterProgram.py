#
#
#
#
#HAVE TO DOCUMENT THIS

import os
import random
import math
import GameWorldCraps
import tictactoe
import GameWorldGuessMyNumber

totalScore = 0
gameChoice = ""

def getPassword():

    # mpk Clear the screen and print password screen
    print()
    print()
    print(' '*10+'='*50+'=')
    print(' '*10+'='*50+'=')
    print(' '*10+'*'+' '*49+'*')
    print(' '*10 + '*' +' '*16+'Enter Game World'+' '*17+'*')
    print(' '*10+'*'+' '*49+'*')
    print(' '*10+'='*50+'=')
    print(' '*10+'='*50+'=')
    print()
    print(' '*10+'*'+' '*49 +'*')

    #mpk Read in User ID and Password
    userName = input('Please enter user ID: ')
    passWord = input('Please enter password: ')

    print('' * 10 + '*' + '' * 49 + '*')

    while userName == '' or passWord == '':
        print('             Please enter a valid userName and passWord.')
        username = input('             Please enter user ID: ')
        passWord = input('             Please enter password: ')

    while passWord != 'h':
        print('            Please enter a valid Password.')
        passWord = input('            Please enter Password: ')

    # mpk Clear the Screen and call the Game Menu function
    while gameChoice != "0":
        cls()
        gameMenu(userName)

####################################################################################
####################################################################################

def gameMenu(UserID):
    #while not gameChoice in ['0', '1', '2', '5']:
        #print('test')

    #mpk Clear the screen and print the Game Menu Screen
    cls()
    print()
    print()
    print()
    print(' '*10+'='*50+'=')
    print(' '*10+'='*50+'=')
    print(' '*10+'*'+' '*49 +'*')

    # mpk Calculate the margins for a message that changes
    greeting = 'Welcome to Game World, ' + UserID + '!'
    greetingLength = (len(greeting))
    margins = ((46 - greetingLength) / 2)
    print(' '*9, '*' + ' '*int(margins), greeting, ' '*int(margins), '*')

    print(' '*10+'*'+' '*49 +'*')
    print(' '*10+'*'+'   0. Exit'+' '*39 +'*')
    print(' '*10+'*'+'   1. Craps'+' '*38 +'*')
    print(' '*10+'*'+'   2. Guess The Number'+' '*27 +'*')
    print(' '*10+'*'+'   3. Word Jumble'+' '*32 +'*')
    print(' '*10+'*'+'   4. Blastoff'+' '*35 +'*')
    print(' '*10+'*'+'   5. Tic-Tac-Toe'+' '*32 +'*')
    print(' '*10+'*'+' '*49 +'*')
    print(' '*10+'*'+' '*49 +'*')

    print(' '*10+'='*50+'=')
    print(' '*10+'='*50+'=')
    print()

    global gameChoice
    # mpk Read in the user's choice of game
    gameChoice = input('          Please choose a game: ')

    # Call the correct game based on the user's choice
    getGame(gameChoice)
####################################################################################
####################################################################################

def getGame(gameChoice):
    screenPause = ' '*12+'Press Enter to continue...'

    while gameChoice != '1' and gameChoice != '2' and gameChoice != '5':
        if gameChoice == '3':
            print()
            print(' '*11, 'Game under construction. Please try again later.')
            input(screenPause)
        elif gameChoice == '4':
            print()
            print(' '*11, 'Game under construction. Please try again later.')
            input(screenPause)
        elif gameChoice == '0':
            quit()
        else:
            print()
            print(' '*11, 'You have entered an invalid menu choice.')


        gameChoice = input('             Please choose a game between 1 and 4: ')

    if gameChoice == '1':
        global totalScore
        crapsScore = GameWorldCraps.Craps()
        cls()
        print()
        if crapsScore > 0:
            print(' '*14, 'Congratulations! Your Craps score is', str(crapsScore) + '.')
        else:
            print(' '*20, 'Your Craps score is', str(crapsScore) + '.')
        totalScore = totalScore + crapsScore
        print(' '*12, 'Your total score for this game session is', str(totalScore) + '.')
        input(screenPause)
    elif gameChoice == '2':
        guessMyNumberScore = GameWorldGuessMyNumber.guessMyNumber()
        totalScore = totalScore + guessMyNumberScore
        input(screenPause)
    elif gameChoice == '5':
        global totalScore
        totalScore += tictactoe.newGame()

    #getGame(gameChoice)
    gameMenu('test')

####################################################################################
####################################################################################

# mpk Declare the Main() function
def Main():
    cls()
    getPassword()
    print()

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


# mpk Call the Main() function
Main()

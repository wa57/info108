#
#
#
#
#

import os
import random
import math

os.system('clear')

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

    # mpk Clear the Screen and call the Game Menu function
    os.system('clear')
    gameMenu(userName)
####################################################################################
####################################################################################

def gameMenu(UserID):

    #mpk Clear the screen and print the Game Menu Screen
    os.system('clear')
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
    print(' '*10+'*'+'   1. Craps'+' '*38 +'*')
    print(' '*10+'*'+'   2. Guess The Number'+' '*27 +'*')
    print(' '*10+'*'+'   3. Word Jumble'+' '*32 +'*')
    print(' '*10+'*'+'   4. Hangman'+' '*36 +'*')
    print(' '*10+'*'+' '*49 +'*')
    print(' '*10+'*'+' '*49 +'*')

    print(' '*10+'='*50+'=')
    print(' '*10+'='*50+'=')
    print()

    # mpk Read in the user's choice of game
    gameChoice = input('          Please choose a game: ')

    # Call the correct game based on the user's choice
    Craps()
####################################################################################
####################################################################################


def Craps():
    # mpk Demonstrates random number generation
    """
    blockcomments
    """
    # mpk Set up the screen


    # mpk generate random numbers 1 - 6
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2

    # mpk Output Results
    print()
    print()
    print()
    print(' '*7+'='*56+'=')
    print(' '*7+'|*   *|'+' '*41+'  |*   *|')
    print(' '*7 + '|  *  | You rolled a', die1, 'and a', die2, 'for a total of', str(total)+ '!' +'  |  *  |')
    print(' '*7+'|*   *|'+' '*41+'  |*   *|')
    #print(' '*7+' -----  You rolled a', die1, 'and a', die2, 'for a total of', str(total)+ '!'+' -----')
    #print()
    print(' '*7+'='*56+'=')


    # mpk Pause the screen
    input(''*10 + 'Press Enter to continue...')

    # mpk Set up the screen Toss #2
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2

    # mpk generate random numbers 1 - 6


    # mpk Output Results
    print()
    print()
    print()
    print(' '*7+'='*56+'=')
    print(' '*7+'|*   *|'+' '*41+'  |*   *|')
    print(' '*7 + '|  *  | You rolled a', die1, 'and a', die2, 'for a total of', str(total)+ '!' +'  |  *  |')
    print(' '*7+'|*   *|'+' '*41+'  |*   *|')
    #print(' '*7+' -----  You rolled a', die1, 'and a', die2, 'for a total of', str(total)+ '!'+' -----')
    #print()
    print(' '*7+'='*56+'=')

    # mpk Pause the screen
    input(''*10 + 'Press Enter to continue...')

    # mpk Set up the screen Toss #3
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2

    # mpk generate random numbers 1 - 6


    # mpk Output Results
    print()
    print()
    print()
    print(' '*7+'='*56+'=')
    print(' '*7+'|*   *|'+' '*41+'  |*   *|')
    print(' '*7 + '|  *  | You rolled a', die1, 'and a', die2, 'for a total of', str(total)+ '!' +'  |  *  |')
    print(' '*7+'|*   *|'+' '*41+'  |*   *|')
    #print(' '*7+' -----  You rolled a', die1, 'and a', die2, 'for a total of', str(total)+ '!'+' -----')
    #print()
    print(' '*7+'='*56+'=')

    # mpk Pause the screen
    input(''*10 + 'Press Enter to continue...')
####################################################################################
####################################################################################

# mpk Declare the Main() function
def Main():
    getPassword()
    print()


# mpk Call the Main() function
Main()

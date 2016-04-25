import os
import random

def Craps():
    # mpk Demonstrates random number generation
    crapsTotal = 0

    # mpk Set up the screen
    os.system('clear')

    # mpk generate random numbers 1 - 6
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    if total == 7 or total == 11:
        crapsTotal = crapsTotal + 1

    # mpk Output Results
    print()
    print()
    print()
    print(' '*7+'='*56+'=')
    print(' '*7+'|*   *|'+' '*41+'  |*   *|')
    printRoll(total, die1, die2)
    print(' '*7+'|*   *|'+' '*41+'  |*   *|')
    print(' '*7+'='*56+'=')


    # mpk Pause the screen
    input(''*10 + 'Press Enter to continue...')

    # mpk Set up the screen Toss #2
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    if total == 7 or total == 11:
        crapsTotal = crapsTotal + 1

    # mpk generate random numbers 1 - 6


    # mpk Output Results
    print()
    print()
    print()
    print(' '*7+'='*56+'=')
    print(' '*7+'|*   *|'+' '*41+'  |*   *|')
    printRoll(total, die1, die2)
    print(' '*7+'|*   *|'+' '*41+'  |*   *|')

    print(' '*7+'='*56+'=')

    # mpk Pause the screen
    input(''*10 + 'Press Enter to continue...')

    # mpk Set up the screen Toss #3
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    if total == 7 or total == 11:
        crapsTotal = crapsTotal + 1

    # mpk generate random numbers 1 - 6


    # mpk Output Results
    print()
    print()
    print()
    print(' '*7+'='*56+'=')
    print(' '*7+'|*   *|'+' '*41+'  |*   *|')
    printRoll(total, die1, die2)
    print(' '*7+'|*   *|'+' '*41+'  |*   *|')
    #print(' '*7+' -----  You rolled a', die1, 'and a', die2, 'for a total of', str(total)+ '!'+' -----')
    #print()
    print(' '*7+'='*56+'=')

    # mpk Pause the screen
    input(''*10 + 'Press Enter to continue...')
    return crapsTotal

def printRoll(total, die1, die2):
    if total > 9:
            print(' '*7 + '|  *  | You rolled a', die1, 'and a', die2, 'for a total of', str(total)+ '!' +' |  *  |')
    else:
            print(' '*7 + '|  *  | You rolled a', die1, 'and a', die2, 'for a total of', str(total)+ '!' +'  |  *  |')

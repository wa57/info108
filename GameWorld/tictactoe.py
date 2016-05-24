import os

#EB - Initializes the totalScore global to keep track of score across multiple games
totalScore = 0

#WA - Returns the game board as a dictionary with each attribute holding an array to form the grid
def initBoard():
    return {
        'a': [' ',' ',' '],
        'b': [' ',' ',' '],
        'c': [' ',' ',' ']
    }

#EB - Prints the tic-tac-toe board with formatting to appear as a traditional tic-tac-toe board
def printBoard(board):
    global totalScore
    cls()
    print(' '*4,'{0:<8} {1:<8} {2:<8} {3:<8}'.format('1', '2', '3', 'Player 1: X'))
    print(' '*30, ' '+'Player 2: O')
    print(' '*30, ' '+'Score Total:', totalScore)
    for key, value in sorted(board.items()):
        printColumnLines()
        print(key, ' '*2,'{0:<8} {1:<8} {2:<8}'.format(value[0] + ' '*4+'|', value[1] + ' '*4+'|', value[2]))
        printColumnLines()
        if key != 'c':
            print(' '*4+'-'*22)

#EB - Prints a line of evenly spaced bars to form the game board's containing cells
def printColumnLines():
    print(' '*10 + '|' + ' ' * 8 + '|')

#WA -
def moveMapper(move, board, player):
    move = list(move)
    row = move[0]
    column = int(move[1]) - 1
    symbol = 'X'
    if(player == 2):
        symbol = 'O'
    if board[row][column] == ' ':
        board[row][column] = symbol
    return board

#EB - Checks each victory condition (rows, columns, diagonals) to determine if there is a winner
def checkVictoryCondition(board):
    if checkDiagonals(board):
        return True
    elif checkRows(board):
        return True
    elif checkColumns(board):
        return True
    return False

#WA - Gathers both possible diagonal win conditions and joins them into a new list to be checked
#     If either diagonal returns uniform, we return True
def checkDiagonals(board):
    diagonal1 = [board['a'][0], board['b'][1], board['c'][2]]
    diagonal2 = [board['c'][0], board['b'][1], board['a'][2]]
    if checkIfUniformList(diagonal1) or checkIfUniformList(diagonal2):
        return True
    return False

#WA - Iterates through each row of the game board and checks if the list contains all of the same character
#     If a row returns uniform, we break out of the loop and return True
def checkRows(board):
    for key, value in sorted(board.items()):
        winningRowFound = checkIfUniformList(value)
        if winningRowFound:
            break
    return winningRowFound

#WA - Iterates over a count of 3, each iteration representing a column of the game board
#     If a column (turned row) returns uniform we break out of the loop and return True
def checkColumns(board):
    #WA - Converts the column to a row for comparison
    for column in range(3):
        newRow = [board['a'][column], board['b'][column], board['c'][column]]
        winningColFound = checkIfUniformList(newRow)
        if winningColFound:
            break
    return winningColFound

#def colToRow(board):

#WA - Converts to set and checks the length, sets cannot have duplicate items.
#     Since we are checking for a single character, the set should only have a length of 1
def checkIfUniformList(myList):
    if ' ' not in myList:
        return len(set(myList)) <= 1
    return False

#WA - The main game loop. The game will enter into the while loop and will only break when a victory condition has been discovered
def gameLoop(board):
    #WA - Defaults the player's turn to 1. This acts as a counter
    playerTurn = 1
    #WA - Checks each row, column, and diagonal for a possible victory condition
    while not checkVictoryCondition(board):
        printBoard(board)
        #WA - Validates and returns user input, this makes sure the player's move if within the grid and is valid
        playerMove = getPlayerMove(playerTurn, board)
        #WA - Maps the input coordinate to the game board as a symbol
        board = moveMapper(playerMove, board, player=playerTurn)
        #WA - Resets the counter if player 2's turn just occurred
        if playerTurn == 2:
            playerTurn = 1
        else:
            playerTurn += 1
    printBoard(board)
    determineWinner(playerTurn)


def getPlayerMove(playerTurn, board):
    playerMove = input('\nPlayer ' + str(playerTurn) + ' turn: ')
    while not validatePlayerMove(playerMove, board):
        playerMove = input('\nPlayer ' + str(playerTurn) + ' turn: ')
    return playerMove

def validatePlayerMove(playerMove, board):
    #WA - Attempts to map the player's move onto the game board. If the input
    #     does not conform to the grid or the grid location is already occupied, it will fail and return False
    try:
        playerMove = list(playerMove)
        if board[playerMove[0]][int(playerMove[1]) - 1] == ' ':
            return True
        print('\nThat location is already occupied.')
    except:
        print('\nInvalid Input. Make sure you entered your move location accurately.')
    return False

#EB - Asks the user if they want to play again. If their input is 'y' True is returned
def replay():
    replay = input('Play again? (y/n): ')
    if replay.lower() == 'y':
        return True
    else:
        return False

#WA - Determines who won and adds the score to the game world total
def determineWinner(playerTurn):
    global totalScore
    if playerTurn == 1:
        player = playerTurn + 1
    else:
        player = playerTurn - 1
        totalScore += 1
    print('\nPlayer', player, 'wins!\n')

#EB - Starts a new game, creates a new game board and enters the main game loop
def newGame():
    board = initBoard()
    gameLoop(board)
    if replay():
        newGame()
    else:
        return totalScore

#WA - Utility method to allow command line clears on Windows and Unix operating systems
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

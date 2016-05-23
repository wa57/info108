import os

board = {
    'a': ['','',''],
    'b': ['','',''],
    'c': ['','','']
}

totalScore = 0

def printBoard(board):
    os.system('clear||cls')
    print(' '*4,'{0:<8} {1:<8} {2:<8}'.format('1', '2', '3'))
    print('-'*30)
    for key, value in sorted(board.items()):
        print('\n' + key, ' '*2,'{0:<8} {1:<8} {2:<8}'.format(value[0], value[1], value[2]))

def moveMapper(move, player):
    move = list(move)
    row = move[0]
    column = int(move[1]) - 1
    symbol = 'X'
    if(player == 2):
        symbol = 'O'
    if board[row][column] == '':
        board[row][column] = symbol

def checkVictoryCondition(board):
    if checkDiagonals(board):
        return True
    elif checkRows(board):
        return True
    elif checkColumns(board):
        return True
    return False

#need to check for O as well
def checkDiagonals(board):
    if(board['a'][0] == 'X' and board['b'][1] == 'X' and board['c'][2] == 'X'):
        return True
    elif(board['a'][2] == 'X' and board['b'][1] == 'X' and board['c'][0] == 'X'):
        return True
    return False

def checkRows(board):
    for key, value in sorted(board.items()):
        winningRowFound = checkIfUniformList(value)
        if winningRowFound:
            break
    return winningRowFound

def checkColumns(board):
    #colToRow()
    #WA - Converts the column to a row for comparison
    for column in range(3):
        newRow = [board['a'][column], board['b'][column], board['c'][column]]
        winningColFound = checkIfUniformList(newRow)
        if winningColFound:
            break
    return winningColFound

#def colToRow(board):

#WA - Converts to set and checks the length, sets cannot have duplicate items. Since we are checking for a single character, the set should only have a length of 1
def checkIfUniformList(myList):
    if '' not in myList:
        return len(set(myList)) <= 1
    return False

playerTurn = 1
while not checkVictoryCondition(board):
    printBoard(board)
    playerMove = input('\nPlayer ' + str(playerTurn) + ' turn: ')
    moveMapper(playerMove, player=playerTurn)
    if playerTurn == 2:
        playerTurn = 1
    else:
        playerTurn += 1

printBoard(board)
if playerTurn == 1:
    print('Player', playerTurn + 1, 'wins!')
else:
    print('Player', playerTurn - 1, 'wins!')
    totalScore += 1
    print(totalScore)


#need to add play again and return to gameworld
#need to reinitialize the board and







#determineVictor(board)

#def determineVictor(board):
    #if(board['a'][0]):

def initBoard():
    print('1 = Black, 2 = Red, 0 = Empty Space')
    print()
    grid = [[0 for number in range(8)] for x in range(8)]
    #grid.append(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
    displayBoard(grid)

def displayBoard(grid):
    for idx, row in enumerate(grid):
         print(idx+1, row)
         if idx == 7:
             print('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')

def initCheckers():
    print('yeah')    

initBoard()
    


# simple sudoku solver

board = [
    [0,9,0,0,0,0,0,2,0],
    [6,0,0,9,0,2,0,0,3],
    [0,0,3,0,5,0,7,0,0],
    [0,4,0,0,1,0,0,3,0],
    [0,0,2,6,0,8,4,0,0],
    [0,3,0,0,2,0,0,5,0],
    [0,0,1,0,4,0,8,0,0],
    [7,0,0,2,0,5,0,0,1],
    [0,2,0,0,0,0,0,7,0]
]
def solver(board):

    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):  # 1 to 9
        if validation(board, i, (row, col)):
            board[row][col] = i  # if valid, add to board

            if solver(board):
                return True

            board[row][col] = 0
    return False

def validation(board, number, position):

    # check row
    for i in range(len(board[0])):  # loop through all col in given row
        if board[position[0]][i] == number and position[1] != i:
            return False

    # check col
    for i in range(len(board[0])):  # loop through all row in given col
        if board[i][position[1]] == number and position[0] != i:
            return False

    # check 3x3 cubes
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == number and (i, j) != position:
                return False

    return True  # if all is fine, return true

def print_board(board):  # printing the soduko board nicely
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - - -')  # draw line for every three rows

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(' | ', end='')  # draw line for every three columns

            if j == 8:  # checking for last position on board
                print(board[i][j])
            else:
                print(str(board[i][j]) + ' ', end='')

def find_empty(board):  # locating zero values in board
    for i in range(len(board)):
        for j in range(len(board[0])):  # length of each row
            if board[i][j] == 0:
                return(i, j)  # row, col
    return None  # no squares equal to zero, return none

solver(board)
print_board(board)


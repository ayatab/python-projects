# sudoku solver with gui

# ALGORITHM: try all numbers and find a number that works, then move onto the next one.
# Keep repeating until the solution cannot be completed, and go back one square and try all numbers possible again.
# Repeat the "going backwards" algorithm until a line is completed.

game_board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


# def is how you make functions in python

# print the game board
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


print_board(game_board)

def find_empty_square(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)

def is_valid(board, number, position):

    # checking validity (no duplicates) for each rule

    # check row
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[0] != i:
            return False

    # check column
    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False

    # check each box
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y * 3, box_y*3 + 3):
        for j in range(box_x*3, box_y*3 + 3):
            if board[i][j] == number and (i, j) != position
                return False

    return True

def solve(board):

    #use recursion to solve

    #base case: we have filled up the board
    
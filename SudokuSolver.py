import numpy as np
EvilSudoku = [[0, 0, 0, 6, 0, 7, 1, 0, 3],
              [0, 2, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 0, 0],
              [6, 0, 0, 3, 4, 0, 0, 0, 0],
              [0, 8, 0, 0, 0, 0, 2, 5, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 2, 5, 9, 0, 0],
              [1, 0, 3, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]]

EvilSudoku2 = [[0, 9, 0, 0, 0, 0, 2, 0, 0],
               [4, 0, 0, 0, 5, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 0, 0, 0, 0],
               [1, 0, 5, 0, 0, 0, 0, 0, 6],
               [0, 0, 0, 3, 0, 2, 7, 0, 0],
               [8, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 3, 0, 7, 0, 0, 0, 0, 0],
               [6, 0, 0, 0, 0, 0, 0, 5, 0],
               [0, 0, 0, 9, 0, 0, 0, 0, 0]]

def empty_cell(sudoku):
    """
    Searches through the sudoku for an empty cell which is represented by a 0
    :param sudoku: Input of a numpy 9x9 array with integers 0-9
    :return: (x,y) coordinates from an empty cell(0), if no empty cells found return false.
    """
    for y in range(len(sudoku)):
        for x in range(len(sudoku[0])):
            if sudoku[y][x] == 0:
                return (x,y)
    return False

def possible_number(sudoku, number, position):
    """
    Searches through a sudoku if a number that is inserted is valid by looking at row, column and box
    :param sudoku: Input of a numpy 9x9 array with integers 0-9
    :param number: The number to search for in row, column and box to find any duplicates
    :param position: The position of number as a tuple (x,y)
    :return:
    """
    # row
    for x in range(len(sudoku[0])):
        if sudoku[position[1]][x] == number and position[0] != x:
            return False

    # column
    for y in range(len(sudoku)):
        if sudoku[y][position[0]] == number and position[1] != y:
            return False

    # box
    # defines what box to look in. up left is 0,0 and down right is 2,2
    x_box = position[0] // 3
    y_box = position[1] // 3

    # Loop through a box and check if there duplicates of number, not counting number itself
    for x in range(x_box*3, x_box*3 + 3):
        for y in range(y_box*3,y_box*3 + 3):
            if sudoku[y][x] == number and (x,y) != position:
                return False
    return True


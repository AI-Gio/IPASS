import csv
import numpy as np
import time
from tkinter import *
start_time = time.time()

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

wtf_sudo = [[0, 0, 0, 0, 0, 0, 0, 2, 3], [6, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 4, 0, 0, 0, 0, 0], [0, 0, 0, 0, 8, 0, 7, 0, 0], [5, 0, 2, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 8, 0, 2, 0, 3, 0, 0, 0], [0, 1, 0, 0, 0, 0, 6, 4, 0], [0, 0, 0, 5, 0, 0, 0, 0, 0]]

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

def valid_number(sudoku, number, position):
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



def smallest_str(dictionary):
    """
    Calculates the smallest string
    :param dictionary: A dictionary with key = (x,y) and value = a string
    :return: The coordinates of the cell with the least amount of possibilities
    """
    min_str_length = 10
    min_co = None
    for co, s in dictionary.items():
        if len(s) < min_str_length:
            min_str_length = len(s)
            min_co = co
    return min_co

def cell_possibilities(sudoku):
    """
    Generates dictionary with all of the coordinates of the cells with its possible numbers
    :param sudoku: Input of a numpy 9x9 array with integers 0-9
    :return: Dictionary with key = (x,y) and value = string with possible numbers
    """
    possib_val= {}
    # loop through sudoku
    for y in range(len(sudoku)):
        for x in range(len(sudoku)):
            valid = ""
            if sudoku[y][x] == 0:
                # if a cell is equal to 0, see what numbers are valid in that cell
                for i in range(1,10):
                    if valid_number(sudoku, i, (x,y)):
                        valid += f"{i}"

                # when all of the valid cells are established, add them to the dictionary
                possib_val[(x,y)] = valid
    return possib_val

def solve_sudoku(sudoku):
    """
    Solves sudoku by using backtracking and Minimum remaining value heuristic
    :param sudoku: Input of a numpy 9x9 array with integers 0-9
    :return: if sudoku is solved, it returns true and the sudoku is updated and ready to be printed.
             Else it returns false to go to the previous cell
    """
    if not empty_cell(sudoku):
        return True
    else:
        column, row = smallest_str(cell_possibilities(sudoku))

    for num in range(1,10):
        if valid_number(sudoku, num, (column,row)):
            sudoku[row][column] = num
            if solve_sudoku(sudoku):
                return True
            sudoku[row][column] = 0
    return False

"..__== Speed check algorithm ==__.."

def dots2zero():
    """
    Reads from a csv file with 81 char long strings, but there are dots on the places where there should be 0
    So write to another csv file with zeros instead of dots
    """
    with open('sudoHardDot.csv','r') as f:
        reader = csv.reader(f)
        with open('sudoHard.csv','w', newline='') as F:
            writer = csv.writer(F)
            for row in reader:
                x = row[0].replace('.','0')
                writer.writerow([x])

def str2array(sudo_str):
    """
    Converts sudoku string into an numpy array
    :param sudo_str: input of a 81 long string with only numbers
    :return: numpy 9x9 array with integers 0-9
    """
    s = sudo_str
    sudoku = []
    for i in range(9):
        sudoku.append(list(map(int,s[:9])))
        s = s[9:]
    return sudoku

def array2str(sudo_array):
    """
    Converts a numpy 9x9 array into a string
    :param sudo_array: Input of a numpy 9x9 array with integers 0-9
    :return: A 81 char long string only with numbers
    """
    sudo_str = ''
    for row in sudo_array:
        for digit in row:
            sudo_str += str(digit)
    return sudo_str

def alg_checker(amount, sudo_file):
    """
    Calculate the average time that the algorithm takes with an amount of sudoku's
    :param amount: Decide how many sudoku's u want to give to the algoritm
    :param sudo_file: CSV file with 81 char long strings
    :return: The average time of the algorithm
    """
    times = []
    with open(f'{sudo_file}') as f:
        reader = csv.reader(f)
        for x,row in enumerate(reader):
            start = time.time()
            if x == 0:
                continue
            if x == amount + 1:
                break
            array = str2array(row[0])
            solve_sudoku(array)
            times.append(time.time() - start)
    print(sum(times)/len(times))
    print(f"Max time: {max(times)},  Min time: {min(times)}")

alg_checker(2, 'sudoku.csv')


"..__== Run Section ==__.."
# solve_sudoku(EvilSudoku2)

print("--- %s seconds ---" % (time.time() - start_time))
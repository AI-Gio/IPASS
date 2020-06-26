import csv
import time

class SudokuSolver:

    @staticmethod
    def empty_cell(sudoku):
        """
        Searches through the sudoku for an empty cell which is represented by a 0
        :param sudoku: Input of a 9x9 array with integers 0-9
        :return: (x,y) coordinates from an empty cell(0), if no empty cells found return false.
        """
        for y in range(len(sudoku)):
            for x in range(len(sudoku[0])):
                if sudoku[y][x] == 0:
                    return (x,y)
        return False

    @staticmethod
    def valid_number(sudoku, number, position):
        """
        Searches through a sudoku if a number that is inserted is valid by looking at row, column and box
        :param sudoku: Input of a 9x9 array with integers 0-9
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

    @staticmethod
    def smallest_str(dictionary):
        """
        Calculates the smallest string in a dictionary
        :param dictionary: A dictionary with key = (x,y) and value = a string
        :return: The coordinates of the cell with the least amount of possibilities and the string of the possibilities of that cell
        """
        min_str_length = 10
        min_co = None
        # Loop through dictionary
        for co, s in dictionary.items():
            # if the string is smaller then min_str_length
            if len(s) < min_str_length:
                # the smallest str length is updated
                min_str_length = len(s)
                # coordinate with for now smallest str is updated
                min_co = co
        return min_co, dictionary[min_co]

    @staticmethod
    def cell_possibilities(sudoku):
        """
        Generates dictionary with all of the coordinates of the cells with its possible numbers
        :param sudoku: Input of a 9x9 array with integers 0-9
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
                        if SudokuSolver.valid_number(sudoku, i, (x, y)):
                            valid += f"{i}"

                    # when all of the valid cells are established, add them to the dictionary
                    possib_val[(x,y)] = valid
        return possib_val

    @staticmethod
    def solve_sudoku(sudoku):
        """
        Solves sudoku by using backtracking and Minimum remaining value heuristic
        :param sudoku: Input of a 9x9 array with integers 0-9
        :return: if sudoku is solved, it returns true and the sudoku is updated and ready to be printed.
                 Else it returns false to go to the previous cell
        """
        if not SudokuSolver.empty_cell(sudoku):
            return True
        else:
            # gives back the place with the least amount of possibilities
            (column, row), least_pos = SudokuSolver.smallest_str(SudokuSolver.cell_possibilities(sudoku))

        # goes through the number of all 9 possibilities
        for num in least_pos:
            if SudokuSolver.valid_number(sudoku, int(num), (column, row)):
                sudoku[row][column] = int(num)
                if SudokuSolver.solve_sudoku(sudoku):
                    return True
                sudoku[row][column] = 0
        return False


    "..__== Speed check algorithm ==__.."

    @staticmethod
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

    @staticmethod
    def str2array(sudo_str):
        """
        Converts sudoku string into an array
        :param sudo_str: input of a 81 long string with only numbers
        :return: 9x9 array with integers 0-9
        """
        s = sudo_str
        if len(s) != 81:
            raise ValueError("The sudoku string isn't 81 chars long")
        for char in s:
            if char not in '1234567890':
                raise ValueError('The sudoku string contains a non valid character')
        sudoku = []
        for i in range(9):
            sudoku.append(list(map(int,s[:9])))
            s = s[9:]
        return sudoku

    @staticmethod
    def array2str(sudo_array):
        """
        Converts a 9x9 array into a string and checks if the array is valid
        :param sudo_array: Input of a 9x9 array with integers 0-9
        :return: A 81 char long string only with numbers
        """
        sudo_str = ''
        if len(sudo_array) != 9:
            raise ValueError("The array isn't 9 rows long")

        for row in sudo_array:
            if len(row) != 9:
                raise ValueError("A row isn't 9 items long")
            for digit in row:
                if str(digit) not in '1234567890':
                    raise ValueError('The array contains an item that is not valid')
                sudo_str += str(digit)
        return sudo_str

    @staticmethod
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
                array = SudokuSolver.str2array(row[0])
                SudokuSolver.solve_sudoku(array)
                times.append(time.time() - start)
        print("\nAverage time: "+ str( sum(times)/len(times)) )
        print(f"Max time: {max(times)},  Min time: {min(times)}")

"..__== Run Section ==__.."
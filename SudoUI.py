import sys, time
import turtle
import SudokuSolver as ss

class SudoUI:

    @staticmethod
    def typePrint(text, speed_sec):
        """
        Writes text in console as if someone is writing it at same time.
        :param text: String as input
        :param speed_sec: Time between characters when written in console
        """
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed_sec)

    @staticmethod
    def mainMenu():
        """
        Will generate a main menu where user can choose different options.
        Implements functions from SudokuSolver.py > class SudokuSolver
        """
        Title = """                                       
                     _____       _     _          _____     _             
                    |   __|_ _ _| |___| |_ _ _   |   __|___| |_ _ ___ ___ 
                    |__   | | | . | . | '_| | |  |__   | . | | | | -_|  _|
                    |_____|___|___|___|_,_|___|  |_____|___|_|\_/|___|_|                                         
        """
        x = """
        Welcome to the sudoku solver!
        What do you want to do?

        A: Tutorial of this program
        B: I would like to solve a sudoku
        C: I want to test the algorithm
        D: I want to exit this program
        """
        SudoUI.typePrint(Title, 0.007)
        SudoUI.typePrint(x, 0.03)

        while True:
            choice = input("Choice: ")
            if choice.upper() == "A":
                tut = """
                Welcome to the tutorial!
                To solve a sudoku press B, you will get to input rows for the sudoku.
                Input the sudoku from left to right. Starting at the top left corner. To submit the row, press enter
                When you want to stop inputting a sudoku. Just submit a non valid input.
                
                When done with inputting the last/9th row of the sudoku. 
                Then you press enter, it will open a window where you can see the solution of your sudoku.
                
                Choose option C to test a set of sudokus on the algorithm (more information when chosen).
                
                Choose option D to exit the Sudoku Solver.
                """
                SudoUI.typePrint(tut, 0.03)

            elif choice.upper() == "B":
                print("""
        Input here the sudoku like this:
        500913720
        With the zero's representing emtpy cells
        A row should exist of 9 numbers (0-9)
                        """)
                while True:
                    try:
                        SudoUI.sudoSolve()
                        break
                    except:
                        print("\nWhat you have inputted is not valid")
                        terminate = input("Do you want to stop inputting the sudoku? (y/n): ")
                        if terminate == "y":
                            break

            elif choice.upper() == "C":
                print("""
        To test the algorithm you can input a name of one of the included csv files and the amount of sudokus you want to test it on.
        
        If you want to test your own set of sudokus, put a csv file between the other csv files.
        In the csv file should be rows that have 81 charactars long numbers. Then you can do the same thing from above and see how fast the algorithm is.
        Example sudoku format: 004300209005009001070060043006002087190007400050083000600000105003508690042910300
                """)
                while True:
                    file = input("Insert the name of the file you want to test, example(sudoku.csv): ")
                    amount = input("Insert the amount of sudokus you want to test: ")
                    try:
                        ss.SudokuSolver.alg_checker(int(amount), file)
                        break
                    except:
                        print("\nOne of your inputs isn't valid\n")
                        stop = input("Do u want to exit this choice? (y/n): ")
                        if stop.lower() == "y":
                            break

            elif choice.upper() == "D":
                goodbye = """
 _____           _    _____           
|   __|___ ___ _| |  | __  |_ _ ___   
|  |  | . | . | . |  | __ -| | | -_|  
|_____|___|___|___|  |_____|_  |___|  
                           |___|  
                """
                SudoUI.typePrint(goodbye, 0.009)
                break
            else:
                print("""
        Thats not an option, try again""")

    # Bron:https://trinket.io/embed/python/c3224e0644#.Xu5E8UUzZPY
    @staticmethod
    def text(message, x, y, size):
        """
        Makes it possible to write on window
        :param message: input of what to write
        :param x: x value where to write on window
        :param y: y value where to write on window
        :param size: text size
        """
        myPen = turtle.Turtle()
        myPen.speed(0)
        myPen.color("#000000")
        myPen.hideturtle()

        FONT = ('Arial', size, 'normal')
        myPen.penup()
        myPen.goto(x, y)
        myPen.write(message, align="left", font=FONT)

    @staticmethod
    def drawGrid(grid):
        """
        Draws a 9x9 grid with numbers on a new window using turtle
        :param grid: Input of a 9x9 array
        """
        myPen = turtle.Turtle()
        myPen.speed(0)
        myPen.color("#000000")
        myPen.hideturtle()
        topLeft_x = -150
        topLeft_y = 150

        intDim = 35
        # Draw grid
        for row in range(0, 10):
            if (row % 3) == 0:
                myPen.pensize(3)
            else:
                myPen.pensize(1)
            myPen.penup()
            myPen.goto(topLeft_x, topLeft_y - row * intDim)
            myPen.pendown()
            myPen.goto(topLeft_x + 9 * intDim, topLeft_y - row * intDim)
        for col in range(0, 10):
            if (col % 3) == 0:
                myPen.pensize(3)
            else:
                myPen.pensize(1)
            myPen.penup()
            myPen.goto(topLeft_x + col * intDim, topLeft_y)
            myPen.pendown()
            myPen.goto(topLeft_x + col * intDim, topLeft_y - 9 * intDim)
        # Writes all numbers in cells on grid
        for row in range(0, 9):
            for col in range(0, 9):
                if grid[row][col] != 0:
                    SudoUI.text(grid[row][col], topLeft_x + col * intDim + 9, topLeft_y - row * intDim - intDim + 8, 18)
        myPen.getscreen().update()

    @staticmethod
    def sudoSolve():
        """
        Asks user to input a sudoku and is validated after.
        Then sudoku is solved and is drawn with turtle in a different window
        The user can close the window from an input.
        Implements functions from SudokuSolver.py > class SudokuSolver
        """
        # Ask user for sudoku
        Sudoku = []
        for i in range(1, 10):
            a1, a2, a3, a4, a5, a6, a7, a8, a9 = list(map(int, input(f"row {i}: ")))
            Sudoku.append([a1, a2, a3, a4, a5, a6, a7, a8, a9])
            if i % 3 == 0:
                print("-----------------")

        # Check if the sudoku is valid
        for y in range(len(Sudoku)):
            for x in range(len(Sudoku[0])):
                if Sudoku[y][x] == 0:
                    continue
                elif not ss.SudokuSolver.valid_number(Sudoku, Sudoku[y][x], (x, y)):
                    raise Exception("The sudoku is not valid")

        ss.SudokuSolver.solve_sudoku(Sudoku)
        if ss.SudokuSolver.empty_cell(Sudoku) != False:
            print("This sudoku is not solvable")
        else:
            SudoUI.drawGrid(Sudoku)
            print("Solved the sudoku!")
        if input("To close the window, press y then enter. Otherwise just wait with answering: ") == 'y':
            turtle.Screen().bye()
        else:
            print("Guess u wanted to close to the window, but had a typo\n")
            turtle.Screen().bye()

SudoUI.mainMenu()





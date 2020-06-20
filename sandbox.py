import sys, time, os
import turtle
import SudokuSolver as SS

def typePrint(text, speed_sec):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed_sec)

def mainMenu():
    Title = """                                       
                 _____       _     _          _____     _             
                |   __|_ _ _| |___| |_ _ _   |   __|___| |_ _ ___ ___ 
                |__   | | | . | . | '_| | |  |__   | . | | | | -_|  _|
                |_____|___|___|___|_,_|___|  |_____|___|_|\_/|___|_|                                         
    """
    x = """
    Welcome to the sudoku solver!
    What do u want to do?
    
    A: Tutorial of this program
    B: I would like to solve a sudoku
    C: I want to exit this program
    """
    typePrint(Title, 0.007)
    typePrint(x, 0.04)

    while True:
        choice = input("Choice: ")
        if choice.upper() == "A":
            # TODO: Make the tutorial for this program
            pass

        elif choice.upper() == "B":
            print("""
    Input here the sudoku like this:
    500913720
    With the zero's representing emtpy cells
                    """)
            while True:
                try:
                    sudoSolve()
                    break
                except:
                    print("What u have inputted is not valid")
                    terminate = input("Do u want to stop the progam? (y/n): ")
                    if terminate == "y":
                        break
        elif choice.upper() == "C":
            break
        else:
            print("""
    Thats not an option, try again""")
# Bron:https://trinket.io/embed/python/c3224e0644#.Xu5E8UUzZPY
def text(message,x,y,size):
    myPen = turtle.Turtle()
    myPen.speed(0)
    myPen.color("#000000")
    myPen.hideturtle()

    FONT = ('Arial', size, 'normal')
    myPen.penup()
    myPen.goto(x,y)
    myPen.write(message,align="left",font=FONT)

def drawGrid(grid):
    myPen = turtle.Turtle()
    myPen.speed(0)
    myPen.color("#000000")
    myPen.hideturtle()
    topLeft_x = -150
    topLeft_y = 150

    intDim=35
    for row in range(0,10):
      if (row%3)==0:
        myPen.pensize(3)
      else:
        myPen.pensize(1)
      myPen.penup()
      myPen.goto(topLeft_x,topLeft_y-row*intDim)
      myPen.pendown()
      myPen.goto(topLeft_x+9*intDim,topLeft_y-row*intDim)
    for col in range(0,10):
      if (col%3)==0:
        myPen.pensize(3)
      else:
        myPen.pensize(1)
      myPen.penup()
      myPen.goto(topLeft_x+col*intDim,topLeft_y)
      myPen.pendown()
      myPen.goto(topLeft_x+col*intDim,topLeft_y-9*intDim)

    for row in range (0,9):
        for col in range (0,9):
          if grid[row][col]!=0:
            text(grid[row][col],topLeft_x+col*intDim+9,topLeft_y-row*intDim-intDim+8,18)
    myPen.getscreen().update()


def sudoSolve():

    # Ask user for sudoku
    Sudoku = []
    for i in range(1,10):
            a1, a2, a3, a4, a5, a6, a7, a8, a9 = list(map(int, input(f"row {i}: ")))
            Sudoku.append([a1, a2, a3, a4, a5, a6, a7, a8, a9])
            if i % 3 == 0:
                print("-----------------")

    # Check if the sudoku is valid
    for y in range(len(Sudoku)):
        for x in range(len(Sudoku[0])):
            if Sudoku[y][x] == 0:
                continue
            elif not SS.valid_number(Sudoku, Sudoku[y][x], (x,y)):
                raise Exception("The sudoku is not valid")
    SS.solve_sudoku(Sudoku)
    drawGrid(Sudoku)
    print("Solved the sudoku!")
    if input("To close the window, press y. Otherwise just wait with answering: ") == 'y':
        turtle.Screen().bye()
    else:
        print("Guess u wanted to close to the window, but had a typo")
        turtle.Screen().bye()

mainMenu()
# 000000000
# 000000900
# 970300000
# 010060500
# 004708002
# 000002006
# 031004000
# 000800167
# 087000000















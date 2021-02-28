"""
Grid functions for Sudoku py
"""

# Required libraries
import arcade
import random

# Import image tools used to create tiles
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from typing import List
from globals import *

def create_grid(size: int) -> List:
    """
    Create a two-dimensional grid and populate it with random data
    """
    if size < 1:
        raise ValueError("Grid size must be positive.")
    #Generate an empty grid
    grid = [[0 for _ in range(size)] for _ in range(size)]
    # Start a list of empty locations
    locations = []
    for row in range (size):
        for column in range (size):
            locations.append((row, column))
    #15 numbers in the grid when is first generated 
    for i in range(15):
        #Find an empty location
        emptyLocation = False
        selected_location = None
        while emptyLocation == False:
            # Out of the possible locations, select one.
            selected_location = random.choice(locations)
            y ,x = selected_location
            print(selected_location)
            print(grid[y][x])
            if(grid[y][x] == 0):
                emptyLocation = True

        #Get a list of possible values in the square
        passible_values = getPossibleValesInSquare(selected_location, grid)
        # Out of the possible values, select one.
        selected_number = random.choice(passible_values)
        y ,x = selected_location
        #Assign the selected location to the selected number
        grid[y][x] = selected_number

    #Print the grid to the console
    print_grid(grid)
    return grid

def print_grid(grid: List):
    """
    Print a two-dimensional grid.

    :param grid:
    :return:
    """
    for row in grid:
        for cell in row:
            print(f"{cell:5}", end="")
        print()
    print()

def squareClicked(x , y) -> tuple:
    """
    Returns the x and y values of the box that was clicked
    or None if the passed coordinates do not correspond to a square
    """
    #Check the click was on the grid and not on the menu
    if(y < MENU_HEIGHT):
        #If the click was on the menu return null
        return None

    #Check that the click did not hit a margin 
    
    #Necesary variables 
    quadrant_width = WINDOW_WIDTH / 3
    quadrant_height  = WINDOW_WIDTH / 3
    #Column width = left margin + square size
    column_width = MARGIN + SQUARE_SIZE
    #Row height = bottom margin + square size
    row_height = MARGIN + SQUARE_SIZE
    
    #Get the position of x in any quadrant
    x_in_quadrant = x % quadrant_width
    #Get the possition of x relative to its clossest column 
    x_in_column = x_in_quadrant % column_width
    #Check if a vertical  margin was clicked
    if(x_in_column < MARGIN):
        #A vertical margin was clicked
        return None
    
    #Get the position of y in any quadrant
    y_in_quadrant = (y - MENU_HEIGHT + MARGIN) % quadrant_height
    #Get the possition of y relative to its clossest row 
    y_in_row = y_in_quadrant % row_height
    #Check if a horizontal margin was clicked 
    if(y_in_row < MARGIN):
        #A horizontal margin was clicked
        return None

    #Find the square that was clicked

    #Get the vertical quadrant 
    quadrant_x = int(x // quadrant_width)
    #Get the horizontal  quadrant 
    quadrant_y = int((y -  MENU_HEIGHT + MARGIN) // quadrant_height)

    #Find the closes column in the quadrant from the click 
    column_in_quadrant  = int(x_in_quadrant //  column_width)
    #Find the closes row in the quadrant from the click 
    row_in_quadrant = int(y_in_quadrant // row_height)

    #The x value is equal to the left  columns from adjacent quardants plus the curent column in the quadrant
    square_x = (quadrant_x * 3) + column_in_quadrant
    #The y value is equal to the bottom  rows from adjacent quardants plus the curent row in the quadrant
    square_y = (quadrant_y * 3) + row_in_quadrant
    
    return (square_y, square_x)

def getPossibleValesInSquare(square, grid):
    """
    Returns the possible vales for a given square
    :param square:
    :param grid:
    :return:
    """
    validNumbers = []
    numbers = {1:True, 2:True, 3:True, 4:True, 5:True, 6:True, 7:True, 8:True, 9:True }
    row, column = square
    #loop through the column and update tha values that have already been used in the column 
    for column_i in range(BOARD_SIZE):
        if(grid[row][column_i] != 0): 
            #Update the object storing the numbers that are valid
            numbers[grid[row][column_i]] = False
    #loop through the row and update tha values that have already been used in the row 
    for row_i in range(BOARD_SIZE):
        if(grid[row_i][column] != 0): 
            #Update the object storing the numbers that are valid
            numbers[grid[row_i][column]] = False

    #Get the index of the first row in the quadrant 
    squareIndexStartRow = (row // 3) * 3
    #Get the index of the first column in the quadrant
    squareIndexStartCol = (column // 3) * 3


    #Loop throw the rows in the quardant 
    for row_check_i in range(squareIndexStartRow, squareIndexStartRow + 3):
        #Loop throw the columns in the quardant
        for column_check_i in range(squareIndexStartCol, squareIndexStartCol + 3):
            #Check if a number has been found
            if(grid[row_check_i][column_check_i] != 0):
                #Update the object storing the numbers that are valid
                numbers[grid[row_check_i][column_check_i]] = False

    for number in range (1, BOARD_SIZE + 1):
        #Check if the number is  valid
        if (numbers[number]):
            #Save it into the valid Numbers array 
            validNumbers.append(number)

    return validNumbers



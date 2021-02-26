"""
Grid functions for Sudoku py
"""

from typing import List
from globals import *

def create_grid(size: int) -> List:
    """
    Create a two-dimensional grid
    """
    if size < 1:
        raise ValueError("Grid size must be positive.")
    grid = [[0 for _ in range(size)] for _ in range(size)]
    return grid

def squareClicked(x , y) -> tuple:
    """
    Returns the x and y values of the box that was clicked
    """
    #Check the click was on the grid and not on the menu
    if(y < MENU_HEIGHT):
        #If the click was on the menu return null
        print('Click on the menu')
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
        print('Clicked vertical margin')
        return None
    
    #Get the position of y in any quadrant
    y_in_quadrant = (y - MENU_HEIGHT + MARGIN) % quadrant_height
    #Get the possition of y relative to its clossest row 
    y_in_row = y_in_quadrant % row_height
    #Check if a horizontal margin was clicked 
    if(y_in_row < MARGIN):
        #A horizontal margin was clicked
        print('Clicked horizontal margin')
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
    
    return (square_x, square_y)





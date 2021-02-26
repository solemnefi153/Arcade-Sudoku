"""
GUI for Sudoky py

Nefi Aguilar
"""

# Required libraries
import math
import arcade

# Import image tools used to create tiles
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from typing import List

# Functions for manipulating the grid
from grid_functions import *

#Import Global variables 
from globals import *



def create_textures() -> List:
    """
    Create a series of images that will be used for each tile in the game.
    :return: List of images
    """
    texture_list = []

    for i in range ((BOARD_SIZE * BOARD_SIZE)) :
        img = Image.new('RGB', (SQUARE_SIZE, SQUARE_SIZE), color=SQUARE_COLORS[2])
        texture = arcade.Texture("0", img)
        texture_list.append(texture)

    return texture_list


def create_grid_sprites() -> arcade.SpriteList:
    """
    Return a SpriteList of Sprites to go on the screen.
    :return:
    """
    my_sprite_grid = arcade.SpriteList()
    width = SQUARE_SIZE
    height = SQUARE_SIZE
    column_square = 2
    row_square = 2
    for row in range(BOARD_SIZE):
        #Adds extra margin every 3 rows
        if((row % 3 == 0)):
            row_square = row_square + 1
            if row_square == 3:
                row_square = 0
        for column in range(BOARD_SIZE):
            my_sprite = arcade.Sprite()
            #Adds extra margin every 3 columns
            if((column % 3 == 0)):
                column_square = column_square + 1
                if column_square == 3:
                    column_square = 0
           
            my_sprite.center_x = column * (width + MARGIN) + width / 2 + MARGIN + (MARGIN * column_square)
            my_sprite.center_y = row * (height + MARGIN) + height / 2 + MARGIN + MENU_HEIGHT + (MARGIN * row_square)

            my_sprite_grid.append(my_sprite)

    return my_sprite_grid


def update_grid_textures(grid: List,
                         sprite_list: arcade.SpriteList,
                         texture_list: List):
    """
    Takes each Sprite in the SpriteList and flips its texture to the appropriate
    one depending on the backing grid.
    :param grid:
    :param sprite_list:
    :param texture_list:
    :return:
    """
    for row_no in range(len(grid)):
        for column_no in range(len(grid[0])):
            if grid[row_no][column_no] == 0:
                index = 0
            else:
                index = int(math.log2(grid[row_no][column_no]))

            loc = row_no * len(grid) + column_no
            # print(f"{row_no} {column_no} => {loc} = {grid[row_no][column_no]}")
            sprite_list[loc].texture = texture_list[index]


class MyGame(arcade.Window):
    """
    Main Game Class
    """
    def __init__(self):
        """
        Initializer for MyGame
        """
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, "Sudoku")
        self.my_grid_sprites = None
        self.my_textures = None
        self.my_grid = None
        self.square_selected = False
        self.square_selected_possible_vales  = []

        arcade.set_background_color(BACKGROUND_COLOR)

    def setup(self):
        """
        Set the game up for play. Call this to reset the game.
        :return:
        """
        self.my_grid_sprites = create_grid_sprites()
        self.my_textures = create_textures()
        self.my_grid = create_grid(BOARD_SIZE)

        # print_grid(self.my_grid)
        update_grid_textures(self.my_grid, self.my_grid_sprites, self.my_textures)


    def on_draw(self):
        """
        Draw the grid
        :return:
        """
        arcade.start_render()
        self.my_grid_sprites.draw()
    
    def on_mouse_press(self, x, y, button, modifiers):
        """
        Handle mouse input
        This function will be use to select grid boxes 
        """
        #Only left clicks are valid
        if (button == arcade.MOUSE_BUTTON_RIGHT):
            return
        #Get the square coordinates
        square_coordinates = squareClicked(x , y)
        #If square_coordinates are not valid, return 
        if (square_coordinates == None):
            return


        #If the square is not empty continue 

        #Oherwise do nothing

        #Highlight the square that is selected 

        #Highlight the row and column with a different color( optional ) 

        #Display possible values 

        #Promt for value

        pass

    def on_key_press(self, symbol: int, modifiers: int):
        """
        Handle key input
        This function will be use to update grid boxes
        """
        #Check if a box is selected 

        #If not do nothing

        #Check the symbol is a number 
        #ASCII 49 is 1  and we want numbers from 1 - 9 
            
        #Else do nothing 

        #Check the number is within the possible numbers

        #Else do nothing

        #Update the box 

        #Deselect the box

        pass

        



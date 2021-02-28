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
from grid_functions import create_grid
from grid_functions import squareClicked
from grid_functions import getPossibleValesInSquare


#Import Global variables 
from globals import *



def create_textures() -> List:
    """
    Create a series of images that will be used for each tile in the game.
    :return: List of images
    """
    texture_list = []

    #Regular texture
    img = Image.new('RGB', (SQUARE_SIZE, SQUARE_SIZE), color=SQUARE_COLORS[0])
    texture = arcade.Texture("0", img)
    texture_list.append(texture)

    #Highlighted  texture
    img = Image.new('RGB', (SQUARE_SIZE, SQUARE_SIZE), color=SQUARE_COLORS[1])
    texture = arcade.Texture("1", img)
    texture_list.append(texture)

    #Highlighted  row / column texture 
    img = Image.new('RGB', (SQUARE_SIZE, SQUARE_SIZE), color=SQUARE_COLORS[2])
    texture = arcade.Texture("2", img)
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

def update_grid_textures(square_selected: tuple, sprite_list: arcade.SpriteList, texture_list: List):
    """
    Takes each Sprite in the SpriteList and assigns its corresponding texture
    :param square_selected:
    :param sprite_list:
    :param texture_list:
    :return:
    """
    for row_no in range(BOARD_SIZE):
        for column_no in range(BOARD_SIZE):
            loc = row_no * BOARD_SIZE + column_no
            #Case when there is not a selected square
            if (square_selected == None):
                sprite_list[loc].texture = texture_list[0]
            else:
                #Case when the sprite is the selected sprite
                if(square_selected[0] == row_no and square_selected[1] == column_no):
                    sprite_list[loc].texture = texture_list[1]
                #Case when the sprite is the row or column of the selected sprite
                elif (square_selected[0] == row_no or square_selected[1] == column_no):
                    sprite_list[loc].texture = texture_list[2]
                #Default case
                else:
                    sprite_list[loc].texture = texture_list[0]

def draw_grid_numbers(grid):
    """
    Updates the numbers that appear on the grid
    :param grid:
    :return:
    """
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
            #Adds extra margin every 3 columns
            if((column % 3 == 0)):
                column_square = column_square + 1
                if column_square == 3:
                    column_square = 0
            if(grid[row][column] != 30):
                text_center_x = column * (width + MARGIN) + width / 2 + MARGIN + (MARGIN * column_square)
                text_center_y = row * (height + MARGIN) + height / 2 + MARGIN + MENU_HEIGHT + (MARGIN * row_square)
                arcade.draw_text(str(grid[row][column]), text_center_x, text_center_y, arcade.color.BLACK, FONT_SIZE, anchor_x="center", anchor_y="center")

def draw_available_numbers(availabel_numbers):
    """
    Updates the numbers that the user is still missing in the grid
    :param availabel_numbers:
    :return:
    """
    for index in range(len(availabel_numbers)):
        if(availabel_numbers[index] != 0):
            number = index + 1
            space_per_number = WINDOW_WIDTH /  len(availabel_numbers)
            space_before_number = space_per_number * index
            text_start_x =  space_before_number +  space_per_number / 2  
            text_start_y = 125
            arcade.draw_text(str(number), text_start_x, text_start_y, arcade.color.WHITE, FONT_SIZE, anchor_x="center", anchor_y="center")

def draw_possible_values(possible_values):
    """
    Shows the numbers that are valid for a square
    :param availabel_numbers:
    :return:
    """
    strValidNumbers = ""
    for number in possible_values:
        strValidNumbers += " " + str(number)
    text_center_x = 20 
    text_center_y = 70
    arcade.draw_text("Valid Numbers:" + strValidNumbers, text_center_x, text_center_y, arcade.color.WHITE, FONT_SIZE)
     

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
        self.square_selected = None
        self.available_numbers = None
        self.square_selected_possible_vales  = None
        arcade.set_background_color(BACKGROUND_COLOR)

    def setup(self):
        """
        Set the game up for play. Call this to reset the game.
        :return:
        """
        self.my_grid_sprites = create_grid_sprites()
        self.my_textures = create_textures()
        self.my_grid = create_grid(BOARD_SIZE)
        self.available_numbers = [BOARD_SIZE for _ in range(BOARD_SIZE)]
        update_grid_textures(self.square_selected, self.my_grid_sprites, self.my_textures)
        
    def on_draw(self):
        """
        Draw the grid
        :return:
        """
        arcade.start_render()
        self.my_grid_sprites.draw()
        draw_grid_numbers(self.my_grid)
        draw_available_numbers(self.available_numbers)
        if(self.square_selected != None):
            draw_possible_values(self.square_selected_possible_vales)

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Handle mouse input
        This function will be use to select grid boxes 
        """
        #Only left clicks are valid
        if (button == arcade.MOUSE_BUTTON_RIGHT):
            return
        #Get the square coordinates
        self.square_selected = squareClicked(x , y)
        #If square_coordinates are not valid end this function
        if (self.square_selected == None):
            #Diselect the grid square and dehighlight the squares 
            update_grid_textures(self.square_selected, self.my_grid_sprites, self.my_textures) 
            self.square_selected_possible_vales = None
            return

        #Check if the square is not empty 
        y , x = self.square_selected
        if (self.my_grid[y][x] != 0):
            #Do not save the selected square
            self.square_selected = None
            #Diselect the grid square and dehighlight the squares 
            update_grid_textures(self.square_selected, self.my_grid_sprites, self.my_textures) 
            self.square_selected_possible_vales = None
            return 

        #Highlight the selected square and its corresponding row and column 
        update_grid_textures(self.square_selected, self.my_grid_sprites, self.my_textures)

        #Safe the possible values 
        self.square_selected_possible_vales =  getPossibleValesInSquare(self.square_selected, self.my_grid)


    def on_key_press(self, symbol: int, modifiers: int):
        """
        Handle key input
        This function will be use to update grid boxes
        """
        #Check if a square is not selected 
        if(self.square_selected == None):
            return

        #Check the symbol is not number 
        #ASCII 49 is 1  and we want numbers from 1 - 9 
        if(symbol < 49 or symbol > 57):
            return 

        newNumber = symbol - 48
        #Check the number is within the possible numbers
        if(newNumber not in self.square_selected_possible_vales):
            return

        #Update the box 
        y, x = self.square_selected
        self.my_grid[y][x] = newNumber

        #Update the available numbers 
        self.available_numbers[newNumber - 1] = self.available_numbers[newNumber - 1] - 1


        #Deselect the box
        self.square_selected = None
        self.square_selected_possible_vales = None


        



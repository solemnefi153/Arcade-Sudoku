"""
Sudoku py

Nefi Aguilar
"""


import arcade

from gui import MyGame


def main():
    my_game = MyGame()
    my_game.setup()
    arcade.run()


if __name__ == "__main__":
    main()

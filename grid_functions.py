"""
Grid functions for Sudoku py
"""

from typing import List

def create_grid(size: int) -> List:
    """
    Create a two-dimensional grid.
    """
    if size < 1:
        raise ValueError("Grid size must be positive.")
    grid = [[0 for _ in range(size)] for _ in range(size)]
    return grid




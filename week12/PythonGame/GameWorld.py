from time import sleep
import os

from WorldObject import WorldObject
from Vector2D import Vector2D
from SnakeParts import SnakeHead
from EmptyCell import EmptyCell
from settings import DeathError
from Food import Flower


class GameWorld():
    def __init__(self, size, contents=None):
        self.matrix = [[EmptyCell(Vector2D(row, col)) for col in range(size)]
                                                      for row in range(size)]

    def print_game(self):
        for line in self.matrix:
            for ch in line:
                print(ch, end=" ")
            print()

    def validate_movement(self, x, y):
        if x < 0 or y < 0:
            raise IndexError
        if x >= len(self.matrix) or y >= len(self.matrix):
            raise IndexError

    @staticmethod
    def check_for_collision(cell_1, cell_2):
        if isinstance(cell_1, SnakeHead) and isinstance(cell_2, Flower):
            return True

        if isinstance(cell_1, SnakeHead) and not isinstance(cell_2, EmptyCell):
            raise DeathError

        return False

    def set_cell(self, cell):
        self.validate_movement(cell.get_x(), cell.get_y())

        self.matrix[cell.get_y()][cell.get_x()] = cell

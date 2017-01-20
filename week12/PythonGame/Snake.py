from random import randint
from time import sleep
import os

from collections import deque
from EmptyCell import EmptyCell
from Vector2D import Vector2D
from GameWorld import GameWorld
from Food import Flower

from SnakeParts import SnakeHead, SnakeBody


class Python:
    def __init__(self, game, start_pos, direction):
        self.game = game

        if direction == 'left':
            cell_pos = Vector2D(start_pos.get_x() + 1, start_pos.get_y())
        elif direction == 'right':
            cell_pos = Vector2D(start_pos.get_x() - 1, start_pos.get_y())
        elif direction == 'up':
            cell_pos = Vector2D(start_pos.get_x(), start_pos.get_y() - 1)
        elif direction == 'down':
            cell_pos = Vector2D(start_pos.get_x(), start_pos.get_y() + 1)

        self.body = deque([SnakeHead(start_pos),
                           SnakeBody(cell_pos)])
        self.refresh_snake()

    def move(self, direction):
        move_by_x = 0
        move_by_y = 0

        if direction == 'up':
            move_by_y = -1
        if direction == 'down':
            move_by_y = 1
        if direction == 'left':
            move_by_x = -1
        if direction == 'right':
            move_by_x = 1

        old_head = self.body[0]
        # print(old_head.get_x() + move_by_x)
        # print(old_head.get_y() + move_by_y)
        # new_head_pos = Vector2D(old_head.get_x() + move_by_x,
        #                         old_head.get_y() + move_by_y)
        # print(new_head_pos)
        # input('')
        # new_head = SnakeHead(new_head_pos)
        new_head = SnakeHead(Vector2D(old_head.get_x() + move_by_x,
                                      old_head.get_y() + move_by_y))
        self.body.appendleft(new_head)
        self.body[1] = SnakeBody(old_head.position)

        curr_cell = self.game.matrix[self.body[0].get_y()]\
                                    [self.body[0].get_x()]

        if not GameWorld.check_for_collision(self.body[0], curr_cell):
            last_cell = self.body.pop()
            reset_cell = EmptyCell(Vector2D(last_cell.get_x(),
                                            last_cell.get_y()))
            self.game.set_cell(reset_cell)
        else:
            self.game.set_cell(Flower(Vector2D(randint(0, 15),
                                               randint(0, 15))))
        self.refresh_snake()

    def refresh_snake(self):
        for part in self.body:
            self.game.set_cell(part)

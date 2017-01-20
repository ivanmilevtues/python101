from WorldObject import WorldObject
from settings import SNAKE_HEAD, SNAKE_CELL


class SnakeHead(WorldObject):
    def __init__(self, position):
        self.ch = SNAKE_HEAD
        self.position = position


class SnakeBody(WorldObject):
    def __init__(self, position):
        self.ch = SNAKE_CELL
        self.position = position

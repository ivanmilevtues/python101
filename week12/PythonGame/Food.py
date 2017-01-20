from WorldObject import WorldObject
from settings import FLOWER


class Flower(WorldObject):
    def __init__(self, position):
        self.ch = FLOWER
        self.position = position

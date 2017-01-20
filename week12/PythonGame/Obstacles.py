from WorldObject import WorldObject
from settings import WALL, EMPTY_CELL
from Vector2D import Vector2D


class BlackHole(WorldObject):
    def __init__(self, position):
        self.position = position
        self.ch = EMPTY_CELL

    def set_ch(self, char):
        self.ch = char


class Wall():
    def __init__(self, game, position, size, orientation):
        self.start_pos = position
        self.game = game

        start_x = self.start_pos.get_x()
        start_y = self.start_pos.get_y()

        self.wall_objects = []

        if orientation == 'x':
            for pos in range(start_x, start_x + size):
                self.wall_objects.append(BlackHole(Vector2D(pos, start_y)))

        elif orientation == 'y':
            for pos in range(start_y, start_y + size):
                self.wall_objects.append(BlackHole(Vector2D(start_x, pos)))

        self.set_chars()
        self.upload_to_map()

    def set_chars(self):
        for wall_obj in self.wall_objects:
            wall_obj.set_ch(WALL)

    def upload_to_map(self):
        for wall_obj in self.wall_objects:
            self.game.set_cell(wall_obj)

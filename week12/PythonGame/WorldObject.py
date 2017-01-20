from settings import EMPTY_CELL


class WorldObject:
    def __init__(self, position):
        self.ch = EMPTY_CELL
        self.position = position

    def get_x(self):
        return self.position.get_x()

    def get_y(self):
        return self.position.get_y()

    def get_position(self):
        return self.position

    def __str__(self):
        return self.ch

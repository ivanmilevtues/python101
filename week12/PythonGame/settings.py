MOVEMENT = {
    'w': 'up',
    's': 'down',
    'a': 'left',
    'd': 'right'
}

SNAKE_CELL = '■'
EMPTY_CELL = '□'
SNAKE_HEAD = '◆'
WALL = '☷'
FLOWER = '❀'


class DeathError(Exception):
    pass


class DirectionError(Exception):
    pass

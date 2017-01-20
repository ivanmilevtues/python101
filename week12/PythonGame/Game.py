# TODO
# Find way for aSync input!

from random import randint
from time import sleep
import os
from getch import getch

from Snake import Python
from GameWorld import GameWorld
from Vector2D import Vector2D
from settings import MOVEMENT, DeathError
from Obstacles import BlackHole, Wall
from Food import Flower


def main():
    game = GameWorld(15)

    snake = Python(game, start_pos=Vector2D(2, 2), direction="left")

    wall = Wall(game, position=Vector2D(4, 4), size=3, orientation='x')
    wall2 = Wall(game, position=Vector2D(10, 10), size=4, orientation='y')

    game.set_cell(Flower(position=Vector2D(randint(0, 15), randint(0, 15))))
    moves = 0
    try:
        while True:
            os.system('clear')
            game.print_game()
            print(snake.body[0].position, "Move:", moves)
            direction = getch()
            moves += 1
            snake.move(MOVEMENT[direction])
    except IndexError:
        print("You've hit the edge of the map!")
    except DeathError:
        print("You've hit a wall or fell into Black hole!")

if __name__ == '__main__':
    main()

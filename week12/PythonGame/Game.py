# TODO
# Find way for aSync input!
# Ask why + is not working!
# Add the log system

from random import randint
import os
from getch import getch

from Snake import Python
from GameWorld import GameWorld
from Vector2D import Vector2D
from settings import MOVEMENT, DeathError
from Obstacles import BlackHole, Wall
from datetime import datetime
from Food import Flower


def generate_log_msg(start_time, score, moves):
    return """Start Time: {0}
End Time: {1}
Score: {2}
Moves: {3}
""".format(start_time, datetime.now().isoformat(), score, moves)


def generate_filenmame():
    filename = 'Scores/'
    filename += datetime.now().isoformat() + '_score.txt'
    return filename


def main():
    game = GameWorld(15)

    snake = Python(game, start_pos=Vector2D(2, 2), direction="left")

    Wall(game, position=Vector2D(4, 4), size=3, orientation='x')
    Wall(game, position=Vector2D(10, 10), size=4, orientation='y')

    game.set_cell(Flower(position=Vector2D(randint(0, 14), randint(0, 14))))
    score = 0
    moves = 0
    start_time = datetime.now().isoformat()
    filename = generate_filenmame()
    try:
        while True:
            game.print_game()
            print('Score:', score)
            print('Moves:', moves)
            score = len(snake.body) - 2
            moves += 1
            direction = getch()
            snake.move(MOVEMENT[direction])
            os.system('clear')
    except IndexError:
        with open(filename, 'w') as f:
            f.write(generate_log_msg(start_time, score, moves))
        f.close()
        print("You've hit the edge of the map!")
        print("You can check your result at {0}".format(filename))
    except DeathError:
        with open(filename, 'w') as f:
            f.write(generate_log_msg(start_time, score, moves))
        f.close()
        print("You've hit a wall or fell into black hole!")
        print("You can check your result at {0}".format(filename))


if __name__ == '__main__':
    main()

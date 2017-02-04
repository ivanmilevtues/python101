# Python Tetris in the console
# Install: sudo apt-get install python python-tk idle python-pmw python-imaging

import time
import os
import sys
import tty
import sys
import termios

FIGURES = [
    ['L', [0, 2], [1, 0], [1, 1], [1, 2]],
    ['Cube', [0, 0], [0, 1], [1, 0], [1, 1]],
    ['Y', [0, 1], [1, 0], [1, 1], [1, 2]],
    ['I', [0, 0], [0, 1], [0, 2], [0, 3]],
    ['Z', [0, 0], [0, 1], [1, 1], [1, 2]],
    ['RZ', [0, 1], [0, 2], [1, 0], [1, 1]]
]


class Figure:

    def __init__(self, rand_num, game_area_x):
        self.x = game_area_x // 2
        self.y = 1  # This is the starting point of the Figure
        self.type = FIGURES[rand_num]  # Generates random figure
        print(self.type)

    def get_coordinates(self):
        result = []
        result.append([[self.x + self.type[1][0], self.y + self.type[1][1]],
                      [self.x + self.type[2][0], self.y + self.type[2][1]],
                      [self.x + self.type[3][0], self.y + self.type[3][1]],
                      [self.x + self.type[4][0], self.y + self.type[4][1]]])
        return result

    def move(self, key):
        if key == 'a':
            self.x -= 1
        elif key == 'd':
            self.x += 1
        self.y += 1


class GameEngine:
    def __init__(self, game_area_x):
        self.y = 50
        self.game_area = []
        self.x = game_area_x
        for i in range(self.y):
            self.game_area.append([' ' for i in range(game_area_x)])
        # print(len(self.game_area))
        for y in range(self.y):
            for x in range(game_area_x):
                # print(x, y)
                if y == 0 or y == self.y - 1:
                    self.game_area[y][x] = '▣'
                elif x == 0 or x == game_area_x - 1:
                    self.game_area[y][x] = '▣'
        self.fig_last_posiotion = []

    def printer(self):
        for i in self.game_area:
            for j in i:
                sys.stdout.write(j)
            sys.stdout.write('\n')

    # FIND WAY FOR USER TO INPUT!
    def player_input(self):
        orig_settings = termios.tcgetattr(sys.stdin)
        tty.setraw(sys.stdin)
        x = 0
        x = sys.stdin.read(1)[0]
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
        return x

    def collision_detect(self, figure):
        figure.move('')
        for coord_list in figure.get_coordinates():
            for coord in coord_list:
                if self.game_area[coord[0]][coord[1]] != ' ':
                    return True
        return False

    def draw(self, coord_list, ch):
        for list_coord in coord_list:
            for x_coord in list_coord:
                self.game_area[x_coord[1]][x_coord[0]] = ch

    def game_area_init(self, figure):
        fig_coord = figure.get_coordinates()
        if len(self.fig_last_posiotion) > 0:
            self.draw(self.fig_last_posiotion, ' ')
        self.draw(fig_coord, 'X')
        self.fig_last_posiotion = fig_coord

    def gameplay(self, figure):
        # player_input()
        # self.game_area_init(figure)
        # print(self.collision_detect(figure))
        if not self.collision_detect(figure):
            self.game_area_init(figure)


def main():
    a = GameEngine(70)
    f1 = Figure(4, 70)
    while True:
        os.system('clear')
        a.gameplay(f1)
        a.printer()
        time.sleep(1)

if __name__ == "__main__":
    main()

from copy import deepcopy
DEAD = '▢'
ALIVE = '▣'
NEIGHBOURS = [[-1, -1], [0, -1], [1, -1],
              [-1, 0], [1, 0],
              [-1, 1], [0, 1], [1, 1]]


class Matrix:
    def __init__(self):
        self.next_generation = [[]]
        self.last_generation = [[]]
        self.acc = []
        for i in range(5):
            acc = [DEAD for k in range(5)]
            self.last_generation.append(deepcopy(acc))
        self.next_generation = deepcopy(self.last_generation)

    def init_cells(self):
        for i in range(int(input("Cells:"))):
            position = input().split(' ')
            self.last_generation[int(position[0])][int(position[1])]

    def generate_next_gen(self):
        for index_y in range(len(self.last_generation)):
            for index_x in range(len(self.last_generation[index_y])):
                a = Cell(index_x, index_y, self.last_generation, self.last_generation[index_y][index_x])
                a.take_neighbours()
                a.change_status()
                self.next_generation[a.y][a.x] = a.status
        print(self.next_generation)
        self.last_generation = deepcopy(self.next_generation)


class Cell:
    def __init__(self, x, y, generation, status):
        self.x = x
        self.y = y
        self.generation = deepcopy(generation)
        self.status = status

    def validate(self, at):
        return (self.x + at[0] >= 0 and self.x + at[0] < 5 and
                self.y + at[1] >= 0 and self.y + at[1] < 5)

    def take_neighbours(self):
        self.neighbours_alive = 0
        for i in NEIGHBOURS:
            if self.validate(i):
                if self.generation[self.y + i[0]][self.x + i[1]] == ALIVE:
                    self.neighbours_alive += 1

    def change_status(self):
        if self.status == ALIVE and self.neighbours_alive < 2:
            self.status = DEAD
            return 0
        elif self.status == ALIVE and self.neighbours_alive < 4:
            self.status = ALIVE
            return 1
        elif self.status == ALIVE and self.neighbours_alive > 3:
            self.status = DEAD
            return 0
        elif self.status == DEAD and self.neighbours_alive == 3:
            self.status = ALIVE
            return 1


def main():
    a = Matrix()
    a.init_cells()
    a.generate_next_gen()


if __name__ == '__main__':
    main()

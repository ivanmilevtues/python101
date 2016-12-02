import pprint
NEIGHBOURS = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def validator(position, row, column):
    return (position[0] >= 0 and position[1] >= 0) and \
           (position[0] < row and position[1] < column)


def strawberries(row, column, days, dead_strawberries=list):
    if row > 10000 or column > 10000 or row < 0 or column < 0:
        raise ValueError
    matrix = [[0 for i in range(column)] for e in range(row)]
    for position in dead_strawberries:
        matrix[position[0]][position[1]] = 1
    pprint.pprint(matrix)
    for i in range(days):
        for y in range(row):
            for x in range(column):
                if matrix[y][x] == 1:
                    # print(x, y)
                    for n in NEIGHBOURS:
                        if validator((y + n[0], x + n[1]), row, column):
                            if matrix[y + n[0]][x + n[1]] != 1:
                                matrix[y + n[0]][x + n[1]] = -1
                            # print(str(x+n[0]) + ' ' + str(y + n[1]))
        for y in range(column):
            for x in range(row):
                matrix[x][y] = 1 if matrix[x][y] == -1 else matrix[x][y]
        pprint.pprint(matrix)
    return sum(1 for r in matrix for el in r if el == 0)


def main():
    print(strawberries(8, 10, 2, [(4, 8), (2, 7)]))


if __name__ == '__main__':
    main()

def take_column(m, i):
    result_list = []
    for row in m:
        result_list.append(row[i])
    # print(result_list)
    return result_list


def sum_list(row):
    result = 0
    for x in row:
        result += x
    return result


def is_list_correct(row):
    check_index = -1
    for a in row:
        check_index += 1
        for my_index in range(check_index + 1, len(row)):
            if row[check_index] == row[my_index]:
                return False
    return True


def subgrid_to_list(m):
    result = []
    for i in m:
        for k in i:
            result.append(k)
    return result


def is_sudoku_solved(m):
    sudoku_sum = sum_list(m[0])
    # Check the Rows
    for i in m:
        if not is_list_correct(i):
            print("List cr")
            return False
        if sudoku_sum != sum_list(i):
            print("Sum 1")
            return False
    # Check the Columns
    for k in range(len(m[0])):
        if not is_list_correct(take_column(m, k)):
            return False
        if sudoku_sum != sum_list(take_column(m, k)):
            return False
    # Check the small Grids
    subgrid = [[0 for x in range(3)] for x in range(3)]
    for x in range(3, 9, 3):
        for y in range(3, 9, 3):
            for i in range(x - 3, x):
                for k in range(y - 3, y):
                    subgrid[x - i - 1][y - k - 1] = m[i][k]
            if not is_list_correct(subgrid_to_list(subgrid)):
                return False
            if sudoku_sum != sum_list(subgrid_to_list(subgrid)):
                return False
    return True


print(is_sudoku_solved([[4, 5, 2, 3, 8, 9, 7, 1, 6],
                        [3, 8, 7, 4, 6, 1, 2, 9, 5],
                        [6, 1, 9, 2, 5, 7, 3, 4, 8],
                        [9, 3, 5, 1, 2, 6, 8, 7, 4],
                        [7, 6, 4, 9, 3, 8, 5, 2, 1],
                        [1, 2, 8, 5, 7, 4, 6, 3, 9],
                        [5, 7, 1, 8, 9, 2, 4, 6, 3],
                        [8, 9, 6, 7, 4, 3, 1, 5, 2],
                        [2, 4, 3, 6, 1, 5, 9, 8, 7]]))

print(is_sudoku_solved([[1, 2, 3, 4, 5, 6, 7, 8, 9],
                        [1, 2, 3, 4, 5, 6, 7, 8, 9],
                        [1, 2, 3, 4, 5, 6, 7, 8, 9],
                        [1, 2, 3, 4, 5, 6, 7, 8, 9],
                        [1, 2, 3, 4, 5, 6, 7, 8, 9],
                        [1, 2, 3, 4, 5, 6, 7, 8, 9],
                        [1, 2, 3, 4, 5, 6, 7, 8, 9],
                        [1, 2, 3, 4, 5, 6, 7, 8, 9],
                        [1, 2, 3, 4, 5, 6, 7, 8, 9]]))

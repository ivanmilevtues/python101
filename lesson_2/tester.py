from copy import copy, deepcopy


def count_substring(haystack, needle):
    result = 0
    current_str = ""
    for index in range(0, len(haystack)):
        current_str += haystack[index]
        if current_str.find(needle) != -1:
            result += 1
            current_str = ""
    return result


def word_counter(matrix, word):
    row = ""
    result = 0
    list_diag = []
    for k in matrix:
        row = take_row(k)
        result += count_substring(row, word)
        result += count_substring(row, word[::-1])
    for i in range(0, len(matrix[0])):
        row = take_column(matrix, i)
        result += count_substring(row, word)
        result += count_substring(row, word[::-1])

    list_diag = diagonal(matrix)
    result += diag_counter(list_diag, word)
    result += diag_counter(list_diag, word[::-1])

    reversed_matrix = matrix_reverse(matrix)
    list_diag = diagonal(matrix)
    result += diag_counter(list_diag, word)
    result += diag_counter(list_diag, word[::-1])
    return result


def take_row(k):
    row = ""
    for char in k:
        row += char
    return row


def take_column(matrix, char_index):
    row = ""
    column = ""
    for i in matrix:
        row = take_row(i)
        column += row[char_index]
    return column


def diagonal(matrix):
    local_matrix = deepcopy(matrix)
    # Ako ne e s deepcopy nqma da raboti
    result = []
    sum_x = sum_y = position_sum = 0
    last_position_sum = 1
    for sum_x in range(0, len(local_matrix)):
        for sum_y in range(len(local_matrix[sum_x])):
            position_sum = sum_x + sum_y
            diag = ""
            for index_x in range(0, len(local_matrix)):
                for index_y in range(0, len(local_matrix[index_x])):
                    if position_sum == index_x + index_y and local_matrix[index_x][index_y] != '.':
                        diag += local_matrix[index_x][index_y]
                        local_matrix[index_x][index_y] = '.'
            if diag != "":
                result.append(diag)
    return result


def diag_counter(diag_list, word):
    result = 0
    for row in diag_list:
        result += count_substring(row, word)
    return result


def matrix_reverse(matrix):
    for x in range(len(matrix)):
        matrix[x] = matrix[x][:: -1]
    return matrix


print(str(word_counter([['i', 'v', 'a', 'n'], ['e', 'v', 'n', 'h'],
                        ['i', 'n', 'a', 'v'], ['m', 'v', 'v', 'n'],
                        ['q', 'r', 'i', 't']], "ivan")))

# TODO make the matrix_input to work!
# def matrix_input():
#     x = int(input("Input X:"))
#     y = int(input("Input Y:"))
#     my_matrix = [[0 for w in range(x)] for h in range(y)]
#     for i in range(x - 1):
#         for k in range(y - 1):
#             my_matrix[i][k] = input()
#     return my_matrix
#
# print(str(matrix_input()))

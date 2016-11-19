def count_substrings(haystack, needle):
    result = 0
    current_str = ""
    for index in range(0, len(haystack)):
        current_str += haystack[index]
        if current_str.find(needle) != -1:
            result += 1
            current_str = ""
    return result

# print(count_substring("Hey", "y"))


def sum_matrix(m):
    result = 0
    for i in m:
        for j in i:
            result += j

    return result

# print(sum_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# print(sum_matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))


def nan_expand(num):
    result = "" #"\""
    for i in range(0, num):
        result += 'Not a '
    if num:
        result += 'NaN'
    return result #+ "\""

# print(nan_expand(0))
# print(nan_expand(1))
print(nan_expand(3))


def prime_number(a):
    is_prime = True
    count = 2
    while count < is_prime:
        if a % count:
            return False
    return True


def getKey(item):
    return item[0]


def prime_factorization(n):
    result_dict = {}
    devider = 2
    while n > 1:
        if n % devider == 0 and prime_number(devider):
            if devider in result_dict:
                result_dict[devider] += 1
            else:
                result_dict[devider] = 1
            n //= devider
            continue
        devider += 1
    return sorted(list(result_dict.items()), key=getKey)

# print(prime_factorization(10))
print(prime_factorization(356))
# print(prime_factorization(89))
# print(prime_factorization(1000))


def group(l):
    result_list = []
    list_index = -1
    for index in range(len(l)):
        if l[index - 1] == l[index] and index != 0:
            # print(list_index)
            result_list[list_index].append(l[index])
        else:
            result_list.append([l[index]])
            list_index += 1
        # print(result_list)
    return result_list

# print(group([1, 1, 1, 2, 3, 1, 1]))


def max_consecutive(items):
    current_max = 1
    overall_max = 0
    for i in range(1, len(items)):
        if items[i - 1] == items[i]:
            current_max += 1
        else:
            current_max = 1
        if current_max > overall_max:
            overall_max = current_max
    return overall_max

# print(max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3]))


def word_counter(matrix, word):
    row = ""
    result = 0
    for k in matrix:
        row = take_row(k)
        result += count_substring(row, word)
        result += count_substring(row, word[::-1])
    for i in range(0, len(matrix[0])):
        row = take_column(matrix, i)
        result += count_substring(row, word)
        result += count_substring(row, word[::-1])
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
    row = ""
    diag = ""
    char_index = 0
    for i in matrix:
        row = take_row(i)
        diag += row[char_index]
        char_index += 1
    return diag


# print("Name" + str(word_counter([['i', 'v', 'a', 'n'], ['e', 'v', 'n', 'h'],
#                                  ['i', 'n', 'a', 'v'],['m', 'v', 'v', 'n'],
#                                  ['q', 'r', 'i', 't']], "ivan")))

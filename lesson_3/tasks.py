import math


def is_number_balanced(number):
    cnt = sum1 = sum2 = 0
    list_nums = []
    while number > 0:
        cnt += 1
        list_nums.append(number % 10)
        number //= 10
    for i in range(0, cnt//2):
        sum1 += list_nums[i]
    for k in range(math.ceil(cnt/2), cnt):
        sum2 += list_nums[k]
    if sum1 == sum2:
        return True
    else:
        return False

# print(is_number_balanced(9))
# print(is_number_balanced(4518))
# print(is_number_balanced(28471))
# print(is_number_balanced(1238033))


def increasing_or_decreasing(seq):
    if seq[0] > seq[1]:
        is_increasing = False
    else:
        is_increasing = True
    for i in range(1, len(seq)):
        if is_increasing:
            if seq[i - 1] >= seq[i]:
                return False
        else:
            if seq[i - 1] <= seq[i]:
                return False
    if is_increasing:
        return "Up!"
    else:
        return "Down!"

# print(increasing_or_decreasing([1, 2, 3, 4, 5, 6]))
# print(increasing_or_decreasing([5, 6, -10]))
# print(increasing_or_decreasing([1, 1, 1, 1]))
# print(increasing_or_decreasing([5, 4, 3, 2]))


def get_largest_palindrome(num):
    for i in range(1, num):
        num -= 1
        if check_palindrom(num):
            return num


def check_palindrom(num):
    my_list = []
    cnt = 0
    while num > 0:
        my_list.append(num % 10)
        num //= 10
        cnt += 1
    for i in range(0, math.ceil(len(my_list) / 2)):
        if i >= (len(my_list) - 1):
            break
        if my_list[i] != my_list[len(my_list) - i - 1]:
            return False
    return True

# print(get_largest_palindrome(99))
# print(get_largest_palindrome(252))
# print(get_largest_palindrome(994687))
# print(get_largest_palindrome(754649))


def sum_of_numbers(st):
    list_index = -1
    is_last_digit = False
    num_list = []
    result = 0
    for i in st:
        if i >= '0' and i <= '9':
            if is_last_digit:
                num_list[list_index] = num_list[list_index] * 10 + int(i)
                is_last_digit = True
            else:
                num_list.append(int(i))
                list_index += 1
                is_last_digit = True
        else:
            # print(i)
            is_last_digit = False
    print(num_list)
    for i in num_list:
        result += i
    return result


# print(sum_of_numbers("ab125cd3"))
# print(sum_of_numbers("ab12"))
# print(sum_of_numbers("1abc33xyz22"))


def birthday_ranges(birthdays, bd_ranges):
    result_list = []
    index = -1
    for tp_range in bd_ranges:
        # print(tp_range)
        result_list.append(0)
        index += 1
        for date in birthdays:
            if date >= tp_range[0] and date <= tp_range[1]:
                result_list[index] += 1
    return result_list

# print("\n" + str(birthday_ranges([1, 2, 3, 4, 5],
#                                  [(1, 2), (1, 3), (1, 4), (1, 5), (4, 6)])))


alphabet_dict = {
    "a": "2",
    "b": "22",
    "c": "222",
    "d": "3",
    "e": "33",
    "f": "333",
    "g": "4",
    "h": "44",
    "i": "444",
    "j": "5",
    "k": "55",
    "l": "555",
    "m": "6",
    "n": "66",
    "o": "666",
    "p": "7",
    "q": "77",
    "r": "777",
    "s": "7777",
    "t": "8",
    "u": "88",
    "v": "888",
    "w": "9",
    "x": "99",
    "y": "999",
    "z": "9999",
    " ": "0"
}


def numbers_to_message(pressed_sequence):

    index = -1
    last_num = -1
    list_key_chain = []
    msg = ''
    next_capital = False
    for i in pressed_sequence:
        if last_num == i and i != -1:
            list_key_chain[index] += str(i)
            last_num = i
        else:
            list_key_chain.append('')
            index += 1
            list_key_chain[index] += str(i)
            last_num = i
    print(list_key_chain)
    for key_chain in list_key_chain:
        if len(key_chain) % 3 != 0 and \
          ((key_chain[0] > '1' and key_chain[0] < '7') or key_chain[0] == '8'):
            value = len(key_chain) % 3 * key_chain[0]
        elif (key_chain[0] > '1' and key_chain[0] < '7') \
                                 or key_chain[0] == '8':
            value = 3 * key_chain[0]
        elif len(key_chain) % 4 != 0:
            value = len(key_chain) % 4 * key_chain[0]
        else:
            value = 4 * key_chain[0]
        if value == '1':
            next_capital = True
        for key in alphabet_dict:
            if alphabet_dict[key] == value:
                if next_capital:
                    msg += key.upper()
                    next_capital = False
                else:
                    msg += key
    return msg

# print(numbers_to_message([1, 7, 7, 7, 8, 8, 2, 2, 9, 9, 9]))
# print(numbers_to_message([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3,
#                           0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2]))


def message_to_numbers(message):
    result_list = []
    last_digit_val = ''
    for char in message:
        for key in alphabet_dict:
            if(char >= 'A' and char <= 'Z'):
                result_list.append(1)
                char = char.lower()
            if char == key:
                if alphabet_dict[key][0] == last_digit_val:
                    result_list.append(-1)
                for digit in alphabet_dict[key]:
                    result_list.append(int(digit))
                last_digit_val = digit
    return result_list

print(message_to_numbers("abc"))
print(message_to_numbers("a"))
print(message_to_numbers("Ivo e Panda"))
# print(message_to_numbers("aabbcc"))

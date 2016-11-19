def bin_search(sorted_list, start, end, srch_value):
    mid = (len(sorted_list) - 1) // 2 if len(sorted_list) % 2 else len(sorted_list) // 2
    if sorted_list[mid] == srch_value:
        return (mid + start)
    elif sorted_list[mid] < srch_value:
        return bin_search(sorted_list[(mid):], mid + start, end, srch_value)
    else:
        return bin_search(sorted_list[:(mid)], start, mid, srch_value)


def turn_point(array, start, end):
    mid = (len(array) - 1) // 2 if len(array) % 2 else len(array) // 2
    if mid < 2 and array[mid] < array[mid - 1]:
        print("What evve")
        return mid + start + 1
    elif mid > len(array) - 2 and array[mid] > array[mid - 1]:
        print("What lsd")
        return mid + start + 1
    if array[mid] < array[mid + 1] and array[mid] > array[mid - 1]:
        return(mid + start + 1)
    elif array[mid] < array[mid + 1]:
        return turn_point(array[mid:], mid + start, end)
    else:
        return turn_point(array[:mid], start, mid)



# Kinda working
# def turn_point(array, start, end):
#     mid = (len(array) - 1) // 2 if len(array) % 2 else len(array) // 2
#     if array[mid] < array[mid + 1] and array[mid] > array[mid - 1]:
#         return(mid + start + 1)
#     elif array[mid] < array[mid + 1]:
#         return turn_point(array[mid:], mid + start, end)
#     else:
#         return turn_point(array[:mid], start, mid)


def main():
    # print(bin_search([1, 2, 3, 4, 5, 6], 0, 5, 1))
    # print(bin_search([1, 2, 3, 4, 5], 0, 4, 2))
    # print(bin_search([1, 2, 3, 4, 5], 0, 4, 3))
    # print(bin_search([1, 2, 3, 4, 5, 6], 0, 5, 4))
    # print(bin_search([1, 2, 3, 4, 5, 6], 0, 5, 5))
    # print(bin_search([1, 2, 3, 4, 5, 6], 0, 5, 6))
    print(turn_point([1, 3, 7, 9, 4, 2], 0, 5))
    print(turn_point([1, 6, 4, 3, 2], 0, 4))


if __name__ == '__main__':
    main()

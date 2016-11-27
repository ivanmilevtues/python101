def binary_search(sorted_list, start, end, srch_value):
    mid = (len(sorted_list) - 1) // 2 if len(sorted_list) % 2 else len(sorted_list) // 2
    if sorted_list[mid] == srch_value:
        return (mid + start)
    elif sorted_list[mid] < srch_value:
        return binary_search(sorted_list[(mid):], mid + start, end, srch_value)
    else:
        return binary_search(sorted_list[:(mid)], start, mid, srch_value)


def find_turning_point(array, start, end):
    mid = (start + end) // 2
    # print(mid, start, end)
    # input()
    # print(mid, len(array) - 1)
    if mid > 0 and mid < len(array) - 1:
        if array[mid - 1] > array[mid] and array[mid + 1] < array[mid]:
            return mid
        elif array[mid - 1] < array[mid]:
            return find_turning_point(array, mid, end)
        else:
            return find_turning_point(array, start, mid)
    elif mid == len(array) - 1:
        if array[mid - 1] > array[mid]:
            return mid
        else:
            find_turning_point(array, mid, end)


def main():
    # print(binary_search([1, 2, 3, 4, 5, 6], 0, 5, 1))
    # print(binary_search([1, 2, 3, 4, 5], 0, 4, 2))
    # print(binary_search([1, 2, 3, 4, 5], 0, 4, 3))
    # print(binary_search([1, 2, 3, 4, 5, 6], 0, 5, 4))
    # print(binary_search([1, 2, 3, 4, 5, 6], 0, 5, 5))
    # print(binary_search([1, 2, 3, 4, 5, 6], 0, 5, 6))
    print(find_turning_point([6, 5, 4, 3, 2, 1], 0, 6))
    print(find_turning_point([1, 3, 7, 9, 4, 2], 0, 6))
    print(find_turning_point([1, 2, 3, 4, 1], 0, 5))
    print(find_turning_point([1, 4, 5, 2], 0, 4))
    print(find_turning_point([1, 6, 4, 3, 2], 0, 5))
    # print(find_turning_point([6, 4, 3, 2], 0, 4))


if __name__ == '__main__':
    main()

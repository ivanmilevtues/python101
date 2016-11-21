def is_credit_card_valid(number):
    digit_list = num_to_list(number)
    if len(digit_list) % 2 == 0:
        return False
    for i in range(len(digit_list) - 1, -1, -1):
        # print(i)
        if i % 2 == 1:
            digit_list[i] = int(digit_list[i]) * 2
            if digit_list[i] > 9:
                digit_list.append(digit_list[i] // 10)
                digit_list[i] = digit_list[i] % 10
        else:
            digit_list[i] = int(digit_list[i])
    if sum(digit_list) != 70:
        return False
    # print(digit_lis)
    return True


def num_to_list(number):
    result = []
    for digit in str(number):
        result.append(digit)
    return result


def main():
    print(is_credit_card_valid(79927398713))
    print(is_credit_card_valid(79927398715))

if __name__ == '__main__':
    main()

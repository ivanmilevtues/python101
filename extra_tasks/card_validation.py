def is_credit_card_vaild(number):
    digit_list = num_to_list(number)
    if len(digit_list) % 2 == 1:
        return False
    else:
        for i in range(len(digit_list)):


def num_to_list(number):
    result = []
    for digit in number:
        result.append(digit)
    return result

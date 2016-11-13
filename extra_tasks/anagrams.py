def are_anagrams(w_1, w_2):
    word_1 = string_to_list(w_1)
    word_2 = string_to_list(w_2)
    if len(word_1) != len(word_2):
        return False
    for i in range(len(word_1)):
        find_char = word_1[i]
        word_1[i] = '.'
        for k in range(len(word_2)):
            if find_char == word_2[k]:
                word_2[k] = '.'
    for i in word_1:
        if i != '.':
            return False
    for i in word_2:
        if i != '.':
            return False
    return True


def string_to_list(st):
    result = []
    for char in st:
        result.append(char)
    return result

print(are_anagrams("TOP_Coder", "Mitka ot bit"))
print(are_anagrams("BRADE", "BEARD"))
print(are_anagrams("silent", "listen"))

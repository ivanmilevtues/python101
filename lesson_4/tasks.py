def simplify_fraction(fraction):
    frac_list = list(fraction)
    a = min(frac_list)
    for i in range(a + 1, 1, -1):
        if frac_list[0] % i == 0 and frac_list[1] % i == 0:
            frac_list[0] //= i
            frac_list[1] //= i
    return tuple(frac_list)

print(simplify_fraction((3, 9)))
print(simplify_fraction((1, 7)))
print(simplify_fraction((4, 10)))
print(simplify_fraction((63, 462)))


def sort_fractions(fraction):
    for i in range(len(fraction)):
        for k in range(i, len(fraction)):
            if(fraction[i][0] / fraction[i][1] > fraction[k][0] / fraction[k][1]):
                fraction[i], fraction[k] = fraction[k], fraction[i]
    return fraction

print(sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]))
print(sort_fractions([(2, 3), (1, 2), (1, 3)]))
print(sort_fractions([(2, 3), (1, 2)]))

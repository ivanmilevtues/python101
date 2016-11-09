class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return "{} / {}".format(self.numerator, self.denominator)

    def __repr__(self):
        return self.__str__()

    def simplify_fraction(self, fraction):
        frac_list = list(fraction)
        a = min(frac_list)
        for i in range(a + 1, 1, -1):
            if frac_list[0] % i == 0 and frac_list[1] % i == 0:
                frac_list[0] //= i
                frac_list[1] //= i
        return tuple(frac_list)

    def __add__(self, other):
        fraction = ()
        fraction = (self.numerator * other.denominator + other.numerator *
                    self.denominator, self.denominator * other.denominator)
        fraction = self.simplify_fraction(fraction)
        return Fraction(fraction[0], fraction[1])

    def __sub__(self, other):
        fraction = ()
        fraction = (self.numerator * other.denominator - other.numerator *
                    self.denominator, self.denominator * other.denominator)
        fraction = self.simplify_fraction(fraction)
        return Fraction(fraction[0], fraction[1])

    def __mul__(self, other):
        fraction = ()
        fraction = (self.numerator * other.numerator, self.denominator *
                    other.denominator)
        fraction = self.simplify_fraction(fraction)
        return Fraction(fraction[0], fraction[1])

    def __eq__(self, other):
        return self.simplify_fraction((self.numerator, self.denominator)) == \
               self.simplify_fraction((other.numerator, other.denominator))


def main():
    a = Fraction(1, 2)
    b = Fraction(2, 4)

    print(a == b)# True
    print(a + b)# 1
    print(a - b)# 0
    print(a * b)# 1 / 4


if __name__ == "__main__":
    main()

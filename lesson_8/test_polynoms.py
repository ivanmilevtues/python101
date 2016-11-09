import unittest
from Polynoms import Polynom, DerivativeCalculate, StringModifier


class Testpolynom(unittest.TestCase):
    def setUp(self):
        self.polynom = Polynom("3x^2+x^2+4x+5x+1")
        self.polynom1 = Polynom("0x^3+4x")
        self.polynom2 = Polynom("20x^36+x^100")

    def test_dict(self):
        self.assertEqual(self.polynom.simplify(), {2: 4, 1: 9})
        self.assertEqual(self.polynom1.simplify(), {3: 0, 1: 4})
        self.assertEqual(self.polynom2.simplify(), {36: 20, 100: 1})

    def test_get_coefficient_power(self):
        self.assertEqual(self.polynom.get_coefficient_power(), [['3', '2'], [1, '2'], ['4', 1], ['5', 1]])
        self.assertEqual(self.polynom1.get_coefficient_power(), [['0', '3'], ['4', 1]])
        self.assertEqual(self.polynom2.get_coefficient_power(), [['20', '36'], [1, '100']])


class TestDerivativeCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = DerivativeCalculate({2: 4, 1: 9})
        self.calc1 = DerivativeCalculate({3: 0, 1: 4})
        self.calc2 = DerivativeCalculate({36: 20, 100: 1})

    def test_calc_der(self):
        self.assertEqual(self.calc.calc_der(), [[8, 1], [9, 0]])
        self.assertEqual(self.calc1.calc_der(), [[0, 2], [4, 0]])
        self.assertEqual(self.calc2.calc_der(), [[100, 99], [720, 35]])


class TestStringModifier(unittest.TestCase):
    def setUp(self):
        self.str = StringModifier([[8, 1], [9, 0]])
        self.str1 = StringModifier([[0, 2], [4, 0]])
        self.str2 = StringModifier([[100, 99], [720, 35]])

    def test___str__(self):
        self.assertEqual(self.str.__str__(), "8x+9")
        self.assertEqual(self.str1.__str__(), "4")
        self.assertEqual(self.str2.__str__(), "100x^99+720x^35")


if __name__ == "__main__":
    unittest.main()

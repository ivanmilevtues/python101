import unittest
from fraction import Fraction


class testFraction(unittest.TestCase):
    def setUp(self):
        self.f1 = Fraction(2, 4)
        self.f2 = Fraction(9, 1)
        self.f3 = Fraction(10, 20)
        self.f4 = Fraction(1, 3)

    def test_simplify_fraction(self):
        self.assertEqual(self.f1.simplify_fraction((2, 4)), (1, 2))
        self.assertEqual(self.f2.simplify_fraction((9, 1)), (9, 1))
        self.assertEqual(self.f3.simplify_fraction((10, 20)), (1, 2))
        self.assertEqual(self.f4.simplify_fraction((1, 3)), (1, 3))

if __name__ == '__main__':
    unittest.main()

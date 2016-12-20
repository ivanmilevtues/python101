import unittest
from decorators import *


class TestDecorator(unittest.TestCase):
    def setUp(self):
        self.expected_result = "Kik sends 3 $!"
        self.expected_result_hello = "Hello, I am Ivan"

    def test_say_hello(self):
        name = "Ivan"
        self.assertEqual(say_hello(name), self.expected_result_hello)
        with self.assertRaises(TypeError):
            say_hello(1)
            say_hello([1, 2, 3, 4])
            say_hello((1, 2))

    def test_deposit(self):
        name = "Kik"
        money = 3
        self.assertTrue(deposit(name, money))
        with self.assertRaises(TypeError):
            deposit(1)
            deposit(['a', 'b', 'c'])
            deposit((1, 'a'))

if __name__ == '__main__':
    unittest.main()

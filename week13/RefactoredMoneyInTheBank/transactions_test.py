import unittest
from transactions import Transaction
from client import Client


class TestTransaction(unittest.TestCase):
    def setUp(self):
        self.a = Client(1, "IVan", 10, "None", "ivan.i.milev@gmail.com")
        self.b = Client(2, "Muhamed", 15, "None", "muhamed@gmail.com")
        self.t = Transaction(self.a)

    def test_deposit(self):
        self.t.deposit(100)
        self.assertEqual(self.a.get_balance(), 110)

    def test_withdraw(self):
        self.assertFalse(self.t.withdraw(100))
        self.t.withdraw(10)
        self.assertEqual(self.a.get_balance(), 0)

    def test_show_balance(self):
        self.assertEqual(str(self.t), "Client: IVan has 10$ in his account.")


if __name__ == '__main__':
    unittest.main()

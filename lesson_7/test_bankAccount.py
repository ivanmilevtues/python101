import unittest
from bankAccount import BankAccount

class testBankAccount(unittest.TestCase):
    def setUp(self):
        self.bankacc = BankAccount("Ivan", 30, '$')

    def test_get_balance(self):
        self.assertEqual(self.bankacc.get_balance(), 30)

    def test___str__(self):
        self.assertEqual(self.bankacc.__str__(), "BankAccount for Ivan with balance of 30$")


if __name__ == '__main__':
    unittest.main()

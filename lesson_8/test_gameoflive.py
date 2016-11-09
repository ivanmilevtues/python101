import unittest
from gameoflife import Matrix, Cell

ALIVE = '▣'
DEAD = '▢'


class TestCell(unittest.TestCase):
    def setUp(self):
        generation = [[DEAD, DEAD, DEAD, DEAD, ALIVE],
                      [ALIVE, DEAD, DEAD, DEAD, ALIVE],
                      [ALIVE, ALIVE, DEAD, DEAD, ALIVE],
                      [DEAD, DEAD, ALIVE, DEAD, DEAD],
                      [DEAD, DEAD, DEAD, DEAD, DEAD]]
        self.cell = Cell(0, 1, generation, ALIVE)
        self.cell1 = Cell(1, 1, generation, DEAD)
        self.cell2 = Cell(2, 3, generation, ALIVE)

    def test_validate(self):
        self.assertEqual(self.cell.validate((-1, -1)), False)
        self.assertEqual(self.cell.validate((0, -1)), True)
        self.assertEqual(self.cell.validate((1, -1)), True)
        self.assertEqual(self.cell.validate((-1, 0)), False)
        self.assertEqual(self.cell.validate((1, 0)), True)
        self.assertEqual(self.cell.validate((-1, 1)), False)
        self.assertEqual(self.cell.validate((0, 1)), True)
        self.assertEqual(self.cell.validate((1, 1)), True)


if __name__ == "__main__":
    unittest.main()

import unittest
from linkedlist import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.l1 = LinkedList()

    def test_add_element(self):
        self.l1.add_element(3)
        self.l1.add_element(4)

        self.assertEqual(self.l1.head.value, 3)
        self.assertEqual(self.l1.tail.value, 4)

    def test_set_elem(self):
        self.l1.add_element(3)
        self.l1.add_element(4)
        self.l1.set_element(1, 2)

        self.assertEqual(self.l1.tail.value, 2)

    def test_index(self):
        self.l1.add_element(3)
        self.l1.add_element(4)

        self.assertEqual(self.l1.index(0).value, 3)
        self.assertEqual(self.l1.index(1).value, 4)
        self.assertFalse(self.l1.index(2))

    def test_size(self):
        self.assertEqual(self.l1.size(), 0)

        self.l1.add_element(3)
        self.l1.add_element(4)

        self.assertEqual(self.l1.size(), 2)

        self.l1.remove(1)
        self.assertEqual(self.l1.size(), 1)

    def test_to_list(self):
        self.l1.add_element(3)
        self.l1.add_element(4)

        self.assertEqual(self.l1.to_list(), [3, 4])

    def test_add_at_index(self):
        self.l1.add_element(3)
        self.l1.add_element(8)

        self.l1.add_at_index(1, 90)
        self.assertEqual(self.l1.index(1).value, 90)

    def test_add_first(self):
        self.l1.add_element(3)
        self.l1.add_element(4)

        self.l1.add_first(8)
        self.assertEqual(self.l1.head.value, 8)

    def test_add_list(self):
        self.l1.add_element(3)
        self.l1.add_element(4)
        self.l1.add_list([5, 6])

        self.assertEqual(self.l1.tail.value, 6)
        self.assertEqual(self.l1.tail.prev.value, 5)

    # def test_add_linked_list(self):
    #     l2 = LinkedList()
    #     self.l1.add_element(3)
    #     self.l1.add_element(4)
    #     l2.add_element(5)
    #     l2.add_element(6)
    #     self.l1.add_linked_list(l2)
    #
    #     # self.assertEqual(self.l1.tail, l2.tail)


if __name__ == '__main__':
    unittest.main()

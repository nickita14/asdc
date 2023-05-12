import unittest

from binary_tree import BinarySearchTree
from binary_listed import DoublyLinkedList
from singly_listed import SinglyLinkedList


class TestLinkedLists(unittest.TestCase):
    def setUp(self):
        self.data = [4, 2, 8, 5, 1]

        self.sll = SinglyLinkedList()
        self.dll = DoublyLinkedList()
        for element in self.data:
            self.sll.insert(element)
            self.dll.insert(element)

    def test_singly_linked_list(self):
        self.assertEqual(self.sll.search(8).data, 8)
        self.sll.remove(5)
        self.assertIsNone(self.sll.search(5))

    def test_doubly_linked_list(self):
        self.assertEqual(self.dll.search(8).data, 8)
        self.dll.remove(5)
        self.assertIsNone(self.dll.search(5))


class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.data = [4, 2, 8, 5, 1]

        self.bst = BinarySearchTree()
        for element in self.data:
            self.bst.insert(element)

    def test_binary_search_tree(self):
        self.assertEqual(self.bst.search(8).data, 8)
        self.bst.delete(5)
        self.assertIsNone(self.bst.search(5))


if __name__ == '__main__':
    unittest.main()
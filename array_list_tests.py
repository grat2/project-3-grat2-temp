import unittest
from array_list import *

class TestCase(unittest.TestCase):
    def test_class(self):
        self.assertEqual(repr(List([None], 1, 0)), "List([None], 1, 0)")
    def test_add(self):
        self.assertRaises(IndexError, add, None, 2, "hole")
        self.assertRaises(IndexError, add, List(["one", "two", 3, 4, "how", None, None, None, None, None], 10, 5), -1, "hi")
        self.assertRaises(IndexError, add, List(["one", "two", 3, 4, "how", None, None, None, None, None], 10, 5), 6, "hi")
        self.assertEqual(add(List(["one", "two", 3, 4, "how", None, None, None, None, None], 10, 5), 4, "hi"), List(["one", "two", 3, 4, "hi", "how", None, None, None, None], 10, 6))
        self.assertEqual(add(List(["one", "two"], 2, 2), 0, "zero"), List(["zero", "one", "two", None], 4, 3))
        self.assertEqual(add(List(["one", "two", None], 3, 2), 2, "three"), List(["one", "two", "three"], 3, 3))
        self.assertEqual(add(List([0, 1, 3, 4, 5], 5, 5), 2, "adding"), List([0, 1, "adding", 3, 4, 5, None, None, None, None], 10, 6))
    def test_length(self):
        self.assertEqual(length(None), 0)
        self.assertEqual(length(List([0, 1, 2, None], 4, 3)), 3)
        self.assertEqual(length(empty_list()), 0)
        self.assertEqual(length(List([1, 3, 5, 7, 9], 5, 5)), 5)
    def test_get(self):
        self.assertRaises(IndexError, get, None, 0)
        self.assertRaises(IndexError, get, List([5, 4], 2, 2), -2)
        self.assertEqual(get(List(["hello", "mabuhay", "aloha", "hi!", None, None], 6, 4), 3), "hi!")
    def test_set(self):
        self.assertRaises(IndexError, set, None, 0, 0)
        self.assertRaises(IndexError, set, List([5, 4], 2, 2), -2, "five")
        self.assertEqual(set(List(["hello", "mabuhay", "aloha", "hi!", None, None], 6, 4), 3, "bye"), List(["hello", "mabuhay", "aloha", "bye", None, None], 6, 4))
    def test_remove(self):
        self.assertRaises(IndexError, remove, None, 0)
        self.assertRaises(IndexError, remove, List([5, 10, 15, 20, None, None], 6, 4), -1)
        self.assertRaises(IndexError, remove, List([5, 10, 15, 20, None, None], 6, 4), 4)
        self.assertEqual(remove(List(["one and only"], 1, 1), 0), ("one and only", List([None], 1, 0)))
        self.assertEqual(remove(List([1, 2, 3, 4, 5], 5, 5), 2), (3, List([1, 2, 4, 5, None], 5, 4)))
        self.assertEqual(remove(List([1, 2, 3, 4, 5], 5, 5), 4), (5, List([1, 2, 3, 4, None], 5, 4)))

class TestList(unittest.TestCase):
    # Note that this test doesn't assert anything! It just verifies your
    # class and function definitions.
    def test_interface(self):
        temp_list = empty_list()
        temp_list = add(temp_list, 0, "Hello!")
        length(temp_list)
        get(temp_list, 0)
        temp_list = set(temp_list, 0, "Bye!")
        remove(temp_list, 0)

if __name__ == '__main__':
    unittest.main()

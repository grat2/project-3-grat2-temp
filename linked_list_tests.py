import unittest
from linked_list import *

class TestCase(unittest.TestCase):
    def test_class(self):
        self.assertEqual(repr(Pair(5, Pair("ten", None))), "Pair(5, Pair('ten', None))")
    def test_empty_list(self):
        self.assertEqual(empty_list(), None)
    def test_add(self):
        self.assertEqual(add(Pair(5, Pair(10, None)), 2, 7.5), Pair(5, Pair(10, Pair(7.5, None))))
        self.assertEqual(add(Pair(5, Pair(10, None)), 1, 7.5), Pair(5, Pair(7.5, Pair(10, None))))
        self.assertEqual(add(Pair(5, Pair(10, None)), 0, 21), Pair(21, Pair(5, Pair(10, None))))
        self.assertEqual(add(Pair(1234, None), 1, 123), Pair(1234, Pair(123, None)))
        self.assertEqual(add(Pair(1234, None), 0, 136), Pair(136, Pair(1234, None)))
        self.assertRaises(IndexError, add, Pair(5, None), 2, "nope")
    def test_length(self):
        self.assertEqual(length(Pair(1, Pair(2, Pair(3, Pair(4, Pair(5, None)))))), 5)
        self.assertEqual(length(None), 0)
        self.assertEqual(length(Pair("what", None)), 1)
    def test_get(self):
        self.assertRaises(IndexError, get, None, 0)
        self.assertRaises(IndexError, get, Pair("what", Pair("pair", Pair("is", Pair("this", None)))), -1)
        self.assertEqual(get(Pair("what", Pair("pair", Pair("is", Pair("this", None)))), 1), "pair")
        self.assertEqual(get(Pair("what", Pair("pair", Pair("is", Pair("this", None)))), 0), "what")
        self.assertEqual(get(Pair("what", Pair("pair", Pair("is", Pair("this", None)))), 3), "this")
    def test_set(self):
        self.assertRaises(IndexError, set, None, 0, "five")
        self.assertRaises(IndexError, set, Pair("what", Pair("pair", Pair("is", Pair("this", None)))), -1, "hi")
        self.assertEqual(set(Pair("what", Pair("pair", Pair("is", Pair("this", None)))), 0, "hi"), Pair("hi", Pair("pair", Pair("is", Pair("this", None)))))
        self.assertEqual(set(Pair("what", Pair("pair", Pair("is", Pair("this", None)))), 2, "hi"), Pair("what", Pair("pair", Pair("hi", Pair("this", None)))))
        self.assertEqual(set(Pair("what", Pair("pair", Pair("is", Pair("this", None)))), 3, "hi"), Pair("what", Pair("pair", Pair("is", Pair("hi", None)))))
    def test_remove(self):
        self.assertRaises(IndexError, remove, None, 0)
        self.assertRaises(IndexError, remove, Pair("what", Pair("pair", Pair("is", Pair("this", None)))), -5)
        list1 = Pair("what", Pair("pair", Pair("is", Pair("this", None))))
        self.assertEqual(remove(list1, 1), ("pair", Pair("what", Pair("is", Pair("this", None)))))

class TestList(unittest.TestCase):
    # Note that this test doesn't assert anything! It just verifies your
    #  class and function definitions.
    def test_interface(self):
        temp_list = empty_list()
        temp_list = add(temp_list, 0, "Hello!")
        length(temp_list)
        get(temp_list, 0)
        temp_list = set(temp_list, 0, "Bye!")
        remove(temp_list, 0)

if __name__ == '__main__':
    unittest.main()

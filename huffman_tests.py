import unittest
import os
from huffman import *

class TestList(unittest.TestCase):

    def test_01_textfile(self):
        s = huffman_encode("textfile.txt", "textfile_encoded.bin")
        self.assertEqual(s, "acb")
        # capture errors by running 'diff' on your encoded file
        # with a *known* solution file
        err = os.system("FC /B textfile_encoded.bin textfile_encoded_soln.bin")
        self.assertEqual(err, 0)

    def test_classes(self):
        hn1 = HuffNode(0, 12, None, None)
        hn2 = HuffNode(0, 12, None, None)
        hl1 = HuffLeaf(0, 12)
        hl2 = HuffLeaf(0, 12)
        self.assertEqual(hn1, hn2)
        self.assertEqual(hl1, hl2)
        self.assertEqual(repr(hn1), "HuffNode({!r}, {!r}, {!r}, {!r})".format(0, 12, None, None))
        self.assertEqual(repr(hl1), "HuffLeaf({!r}, {!r})".format(0, 12))

    def test_huffman_encoding(self):
        s1 = huffman_encode("all_as.txt", "all_as_encoded.bin")
        self.assertEqual(s1, "a")
        err1 = os.system("FC /B all_as_encoded.bin all_as_encoded_sol.bin")
        self.assertEqual(err1, 0)

    def test_huffman_decode(self):
        huffman_decode("all_as_encoded_sol.bin", "all_as_new.txt")
        #err1 = os.system("FC all_as_new.txt all_as_new_sol.txt")
        #self.assertEqual(err1, 0)

if __name__ == '__main__':
   unittest.main()

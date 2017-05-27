from array_list import *

# filename -> list
# counts the occurrences of all characters within a file
def count_occurrence(fName):
    f1 = open(fName)
    l1 = List([0] * 256, 256, 256)
    for line in f1:
        for c in line:
            temp = get(l1, ord(c))
            l1 = set(l1, ord(c), temp + 1)
    return l1

# a HuffmanTree is either a:
# - HuffNode(char, count, left, right)
# - HuffLeaf(char, count)
class HuffNode:
    def __init__(self, char, count, left, right):
        self.char = char # a character (ASCII value)
        self.count = count # an integer
        self.left = left # a HuffmanTree
        self.right = right # a HuffmanTree
    def __eq__(self, other):
        return (type(other) == HuffNode
                and self.char == other.char
                and self.count == other.count
                and self.left == other.left
                and self.right == other.right)
    def __repr__(self):
        return "HuffNode({!r}, {!r}, {!r}, {!r})".format(self.char, self.count, self.left, self.right)

class HuffLeaf:
    def __init__(self, char, count):
        self.char = char # a character (ASCII value)
        self.count = count # an integer
    def __eq__(self, other):
        return (type(other) == HuffLeaf
                and self.char == other.char
                and self.count == other.count)
    def __repr__(self):
        return "HuffLeaf({!r}, {!r})".format(self.char, self.count)

# HuffmanTree -> iterator
# creates an iterator for the given HuffmanTree; helper function for huff_str
def huff_iter(huffmantree):
    if(type(huffmantree) != HuffLeaf):
        yield huffmantree.char
        yield from huff_iter(huffmantree.left)
        yield from huff_iter(huffmantree.right)
    else:
        yield huffmantree.char

# HuffmanTree -> str
# creates a string of all characters in the given HuffmanTree
def huff_str(huffmantree):
    iter1 = huff_iter(huffmantree)
    ret = ""
    for val in iter1:
        ret.append(val)
    return ret

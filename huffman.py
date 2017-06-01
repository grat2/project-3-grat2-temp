import array_list
import linked_list
from huffman_bits_io import *

# filename -> array_list
# counts the occurrences of all characters within a file
def count_occurrence(fName):
    f1 = open(fName)
    l1 = array_list.List([0] * 256, 256, 256)
    for line in f1:
        for c in line:
            temp = array_list.get(l1, ord(c))
            l1 = array_list.set(l1, ord(c), temp + 1)
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
        ret += val
    return ret

# HuffmanTree HuffmanTree -> boolean
# compares two HuffmanTrees and returns True if the first comes before the second and False otherwise
def comes_before(a, b):
    if(a.count < b.count):
        return True
    elif(a.count == b.count and a.char < b.char):
        return True
    else:
        return False

# array_list -> HuffmanTree
# creates a HuffmanTree from the given occurrences of characters in a file
def build_HuffTree(a_list):
    a_iter = array_list.array_iter(a_list)
    sorted_Llist = linked_list.empty_list()
    for val in a_iter:
        if(val[0] != 0):
            sorted_Llist = linked_list.insert_sorted(sorted_Llist, HuffLeaf(val[1], val[0]), comes_before)
    while linked_list.length(sorted_Llist) > 1:
        temp1 = linked_list.remove(sorted_Llist, 0)
        hL1 = temp1[0]
        sorted_Llist = temp1[1]
        temp2 = linked_list.remove(sorted_Llist, 0)
        hL2 = temp2[0]
        sorted_Llist = temp2[1]
        tempChar = 0
        if(hL1.char < hL2.char):
            tempChar = hL1.char
        else:
            tempChar = hL2.char
        hLParent = HuffNode(tempChar, hL1.count + hL2.count, hL1, hL2)
        sorted_Llist = linked_list.insert_sorted(sorted_Llist, hLParent, comes_before)
    tempFinal = linked_list.remove(sorted_Llist, 0)
    return tempFinal[0]

# HuffmanTree -> array_list
# creates a list of character codes from the given HuffmanTree
def build_char_codes(huffTree):
    char_list = array_list.List([""] * 256, 256, 256)
    h_iter = char_huff_iter(huffTree)
    for hT in h_iter:
        char_list = array_list.set(char_list, hT[0], hT[1])
    return char_list

# HuffmanTree -> iterator
# helper iterator to return character codes
def char_huff_iter(huffTree, code = ""):
    if(type(huffTree) != HuffLeaf):
        yield (huffTree.char, code)
        yield from char_huff_iter(huffTree.left, code + "0")
        yield from char_huff_iter(huffTree.right, code + "1")
    else:
        yield (huffTree.char, code)

# str str -> str
# encodes the first (input) file into the second (output) file using Huffman encoding and returns a string of characters used in the first
def huffman_encode(f1, f2):
    o_l = count_occurrence(f1)
    h_t = build_HuffTree(o_l)
    numCodes = num_leaves(h_t)
    char_codes = build_char_codes(h_t)
    tempF = open(f2, "wb")
    tempF.seek(0)
    tempF.truncate()
    tempF.close()
    hb_writer = HuffmanBitsWriter(f2)
    hb_writer.write_byte(numCodes) # write number of codes as a single byte
    tempIter = array_list.array_iter(o_l)
    for val in tempIter: # write c n pairs
        if(val[0] > 0):
            hb_writer.write_byte(val[1]) # write ASCII character code
            hb_writer.write_int(val[0]) # write number of occurrences of character
    tempIter2 = array_list.array_iter(char_codes)
    tempFile = open(f1)
    for line in tempFile:
        for c in line:
            tempCode = array_list.get(char_codes, ord(c))
            hb_writer.write_code(tempCode)
    tempFile.close()
    hb_writer.close()
    tempStrIter = str_huff_iter(h_t)
    tempStr = ""
    for char in tempStrIter:
        tempStr += char
    return tempStr

# HuffmanTree -> iterator
# helper iterator for huffman_encode
def str_huff_iter(huffTree):
    if(type(huffTree) == HuffNode):
        yield from str_huff_iter(huffTree.left)
        yield from str_huff_iter(huffTree.right)
    else:
        yield chr(huffTree.char)

# HuffmanTree -> int
# returns the number of leaves in the HuffmanTree
def num_leaves(huffTree):
    if(type(huffTree) == HuffLeaf):
        return 1
    else:
        return num_leaves(huffTree.left) + num_leaves(huffTree.right)

# str str -> None
# decodes the first (input) file and puts the resulting code into the second (output) file using huffman decoding
def huffman_decode(f1, f2):
    return None

if(__name__ == "__main__"):
    occur_list_1 = count_occurrence("file0.txt")
    huffTree1 = build_HuffTree(occur_list_1)
    print(huffTree1)
    c_list_1 = build_char_codes(huffTree1)
    print(c_list_1)
    retStr = huffman_encode("file0.txt", "file0_encoded.bin")
    print(retStr)

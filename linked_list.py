# an AnyList is either:
# - Pair(first, rest), or
# - None
class Pair:
    def __init__(self, first, rest):
        self.first = first # any value
        self.rest = rest # an AnyList
    def __eq__(self, other):
        return (type(other) == Pair
                and self.first == other.first
                and self.rest == other.rest)
    def __repr__(self):
        return "Pair({!r}, {!r})".format(self.first, self.rest)

# None -> AnyList
# takes in no arguments and returns an empty list
def empty_list():
    return None

# AnyList integer value -> AnyList
# takes in an AnyList, an integer index, and a value and returns a new AnyList
# with the value added at the given index
def add(anylist, index, value, i = 0):
    if(index < 0 or (anylist == None and i < index)):
        raise IndexError()
    elif(i == index and (anylist != None)):
        return Pair(value, Pair(anylist.first, anylist.rest))
    elif(i == index and anylist == None):
        return Pair(value, None)
    else:
        return Pair(anylist.first, add(anylist.rest, index, value, i + 1))

# AnyList -> integer
# takes in an AnyList and returns the length of the list
def length(anylist):
    if(anylist == None):
        return 0
    else:
        return 1 + length(anylist.rest)

# AnyList integer -> value
# takes in an integer index and an AnyList and returns the value at the given
# index in the given AnyList
def get(anylist, index, i = 0):
    if(index < 0 or anylist == None):
        raise IndexError()
    elif(i == index):
        return anylist.first
    else:
        return get(anylist.rest, index, i + 1)

# AnyList integer value -> AnyList
# takes in an AnyList, an integer index, and a value and sets the value at the
# given index in the given AnyList to the new given value
def set(anylist, index, value, i = 0):
    if(index < 0 or anylist == None):
        raise IndexError()
    elif(i == index):
        return Pair(value, anylist.rest)
    else:
        return Pair(anylist.first, set(anylist.rest, index, value, i + 1))

# AnyList integer -> (value, AnyList)
# takes in an AnyList and an integer index and removes the value at the given index and returns a
# tuple containing the value removed and the resulting list
def remove(anylist, index, i = 0, newList = None):
    if(i == 0):
        newList = actual_remove(anylist, index)
    if(index < 0 or anylist == None):
        raise IndexError()
    elif(i == index):
        return (anylist.first, newList)
    else:
        return remove(anylist.rest, index, i + 1, newList)

# AnyList integer -> AnyList
# helper function for remove() that actually modifies the original list by removing the value at
# the given index
def actual_remove(anylist, index, i = 0):
    if(index < 0 or anylist == None):
        raise IndexError()
    elif(i == index):
        return anylist.rest
    else:
        return Pair(anylist.first, actual_remove(anylist.rest, index, i + 1))

# AnyList value comes_before -> AnyList
# inserts a value into a list based on the comes_before function
def insert_sorted(anylist, value, c_b):
    if(anylist == None):
        return Pair(value, None)
    elif(c_b(value, anylist.first) == True):
        return Pair(value, anylist)
    else:
        return Pair(anylist.first, insert_sorted(anylist.rest, value, c_b))

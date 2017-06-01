# an AnyList is one of
# - List(values, capacity, length)
# - None
class List():
    def __init__(self, values, capacity, length):
        self.values = values
        self.length = length
        self.capacity = capacity
    def __eq__(self, other):
        return (type(other) == List
            and self.values == other.values
            and self.length == other.length
            and self.capacity == other.capacity)
    def __repr__(self):
        return "List({!r}, {!r}, {!r})".format(self.values, self.capacity, self.length)

# None -> AnyList
# returns an empty AnyList
def empty_list():
    return List([None], 1, 0)

# AnyList -> AnyList
# a helper function that increases the capacity of the list and returns the new list
def grow_list(anylist):
    if(anylist == None):
        return List([None], 1, 0)
    newList = List([None] * anylist.capacity * 2, anylist.capacity * 2, anylist.length)
    i = 0
    while(i < anylist.length):
        newList.values[i] = anylist.values[i]
        i = i + 1
    return newList

# AnyList index value -> AnyList
# returns a new list with the given value added to the given list at the given index
def add(anylist, index, value):
    if(anylist == None or index < 0 or index > anylist.length):
        raise IndexError()
    if(anylist.length == anylist.capacity):
        anylist = grow_list(anylist)
    i = anylist.length
    while(i > index):
        anylist.values[i] = anylist.values[i-1]
        i = i - 1
    anylist.values[index] = value
    anylist.length = anylist.length + 1
    return anylist

# AnyList -> integer
# returns the length of the given list
def length(anylist):
    if(anylist == None):
        return 0
    i = 0
    lenOfList = 0
    while(i < anylist.capacity and anylist.values[i] != None):
        lenOfList = lenOfList + 1
        i = i + 1
    anylist.length = lenOfList
    return lenOfList

# AnyList index -> value
# returns the value at the given index in the given list
def get(anylist, index):
    if(anylist == None or index < 0 or index >= anylist.length):
        raise IndexError()
    else:
        return anylist.values[index]

# AnyList index value -> AnyList
# returns a list with the value at the given index replaced with the given value
def set(anylist, index, value):
    if(anylist == None or index < 0 or index >= anylist.length):
        raise IndexError()
    anylist.values[index] = value
    return anylist

# AnyList index -> AnyList
# returns a tuple with the removed value and a list with the value at the given index removed
def remove(anylist, index):
    if(anylist == None or index < 0 or index >= anylist.length):
        raise IndexError()
    else:
        i = index
        rem = anylist.values[i]
        while(i < anylist.length - 1):
            anylist.values[i] = anylist.values[i + 1]
            i = i + 1
        anylist.values[anylist.length-1] = None
        anylist.length = anylist.length - 1
        return (rem, anylist)

# AnyList -> iterator
# creates an iterator for an AnyList
def array_iter(anylist, ind = 0):
    if(ind < anylist.length):
        yield (anylist.values[ind], ind)
        yield from array_iter(anylist, ind + 1)

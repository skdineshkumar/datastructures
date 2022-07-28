#A basic hashmap class in python3. This will work like a dictionary in Python
"""
Builtin funcions used:
ord() = This python builtin function returns the number representing the unicode of a specified charaacter

User defined variables:
arr = array/list
loc = location of the key in the array

"""


class Hashmap:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for i in key:
            hash += ord(i)
        return hash % self.MAX

    def __setitem__(self, key, val):
        loc = self.get_hash(key)
        self.arr[loc] = val
    
    def __getitem__(self, key):
        loc = self.get_hash(key)
        return self.arr[loc]

    def __delitem__(self, key):
        loc = self.get_hash(key)
        self.arr[loc] = None




#Collision handling in Hashmap wih linked list. This will work like a dictionary in Python
"""
Builtin functions used:
ord() = This python builtin function returns the number representing the unicode of a specified character

User defined variables:
arr = array/list
loc = location of the key in the array

"""



class Hashmap:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for i in key:
            hash += ord(i)
        return hash % self.MAX

    def __setitem__(self, key, value):
        loc = self.get_hash(key)
        found = False
        for index, element in enumerate(self.arr[loc]):
            if element[0] == key:
                self.arr[loc][index] = (key, value)
                found = True
                break
        if not found:
            self.arr[loc].append((key,value))

    def __getitem__(self, key):
        loc = self.get_hash(key)
        for element in self.arr[loc]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        loc = self.get_hash(key)
        for index, element in enumerate(self.arr[loc]):
            if element[0] == key:
                self.arr[loc].pop(index)





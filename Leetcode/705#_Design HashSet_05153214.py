
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_set = [False]*1000001

    def add(self, key):
        self.hash_set[key] = True

    def remove(self, key):
        self.hash_set[key] = False

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        """
        return self.hash_set[key]



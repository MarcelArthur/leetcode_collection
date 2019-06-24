#!python3
# Design HashSet


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.capacity = 100
        self.storage = [[] for _ in range(self.capacity)]

    def hashfound(self, key):
        return key % self.capacity

    def add(self, key: int) -> None:
        if key not in self.storage[self.hashfound(key)]:
            self.storage[self.hashfound(key)].append(key)

    def remove(self, key: int) -> None:
        if key in self.storage[self.hashfound(key)]:
            self.storage[self.hashfound(key)].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.storage[self.hashfound(key)]

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

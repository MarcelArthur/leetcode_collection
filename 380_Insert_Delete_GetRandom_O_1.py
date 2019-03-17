from random import random
class RandomizedSet:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.random_set = set()
        

#     def insert(self, val: int) -> bool:
#         """
#         Inserts a value to the set. Returns true if the set did not already contain the specified element.
#         """
#         if val not in self.random_set:
#             self.random_set.add(val)
#             return True
#         return False

#     def remove(self, val: int) -> bool:
#         """
#         Removes a value from the set. Returns true if the set contained the specified element.
#         """
#         if val in self.random_set:
#             self.random_set.remove(val)
#             return True
#         return False

#     def getRandom(self) -> int:
#         """
#         Get a random element from the set.
#         """
#         return random.choice(list(self.random_set))
    
    
    # Solution 1:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.A = []
        self.d = {}
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.d:
            n = len(self.A)
            self.A.append(val)
            self.d[val] = n
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.d:
            return False
        
        idx = self.d[val]
        x = self.A[-1]
        if x != val:
            self.A[-1], self.A[idx] = self.A[idx], self.A[-1]
            self.d[x] = idx
        
        self.A.pop()
        del self.d[val]
        return True
        
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        r = random()
        n = len(self.A)
        idx = int(r*n)
        return self.A[idx]
        
    # Solution 2:
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.random_set = dict()
        

#     def insert(self, val: int) -> bool:
#         """
#         Inserts a value to the set. Returns true if the set did not already contain the specified element.
#         """
#         if val not in self.random_set:
#             self.random_set[val] = 0
#             return True
#         return False

#     def remove(self, val: int) -> bool:
#         """
#         Removes a value from the set. Returns true if the set contained the specified element.
#         """
#         if val in self.random_set:
#             self.random_set.pop(val)
#             return True
#         return False

#     def getRandom(self) -> int:
#         """
#         Get a random element from the set.
#         """
#         return list(self.random_set.keys())[randint(0, len(self.random_set) - 1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

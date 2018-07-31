# 在AC的边缘疯狂试探
import random
class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.quicklyData = collections.defaultdict(list) 

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        status = True
        if self.quicklyData.get(val, []):
            status = False
        self.quicklyData[val].append(val)
        return status
        

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if not self.quicklyData.get(val, []):
            return False
        self.quicklyData[val].pop()
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        res = []
        quickly_values =  [res.extend(x) for x in self.quicklyData.values()]
        return random.choice(res)

    
# 社区高效实现方法
# 维护一个列表和高效的hashmap记录index，列表查找的时间复杂度是O(N), 可以通过hashmap记录对应的位置, 快速调换list中对应元素和末尾元素的位置，之后removew就是O(1), 剩下的list插入和随机出一个元素是O(1),所以速度可以满足需求
# 自惭形秽.jpg, 事实证明 更简洁的数据结构实现起来效果可能更好
# import random

# class RandomizedCollection:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.vals = []
#         self.idxs = collections.defaultdict(set)

#     def insert(self, val):
#         """
#         Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
#         :type val: int
#         :rtype: bool
#         """
#         self.vals.append(val)
#         self.idxs[val].add(len(self.vals)-1)
#         return len(self.idxs[val]) == 1
        

#     def remove(self, val):
#         """
#         Removes a value from the collection. Returns true if the collection contained the specified element.
#         :type val: int
#         :rtype: bool
#         """
#         if self.idxs[val]:
#             out = self.idxs[val].pop()
#             ins = self.vals[-1]
#             self.vals[out] = ins
#             if self.idxs[ins]:
#                 self.idxs[ins].add(out)
#                 self.idxs[ins].discard(len(self.vals)-1)
#             self.vals.pop()
#             return True
#         return False
                

#     def getRandom(self):
#         """
#         Get a random element from the collection.
#         :rtype: int
#         """
#         return random.choice(self.vals)

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

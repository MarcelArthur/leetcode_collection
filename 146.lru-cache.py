#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = {}
        self.before, self.next = {}, {}
        self.head, self.tail = "#", "$"
        self.connect(self.head, self.tail)

    def connect(self, head, tail):
        self.next[head], self.before[tail] = tail, head

    def append(self, key, value):
        self.cache[key] = value
        self.connect(self.before[self.tail], key)
        self.connect(key, self.tail)
        if len(self.cache) > self.size:
            self.delete(self.next[self.head])
        
    def delete(self, key):
        self.connect(self.before[key], self.next[key])
        del self.before[key], self.next[key], self.cache[key]

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        result = self.cache[key]
        self.delete(key)
        self.append(key, result)
        return result

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete(key)
        self.append(key, value)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end


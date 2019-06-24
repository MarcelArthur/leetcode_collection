import heapq
import bisect
from typing import List

class KthLargest:
    """
    Time O(N)  Space O(N) Search O(N)
    """

    def __init__(self, k: int, nums: List[int]):
        self.res = []
        self.k = k
        for i in nums:
            if len(self.res) < k:
                heapq.heappush(self.res, i)
            else:
                heapq.heappushpop(self.res, i)

    def add(self, val: int) -> int:
        if len(self.res) < self.k:
            heapq.heappush(self.res, val)
        else:
            heapq.heappushpop(self.res, val)
        return self.res[0]


# Solution 2
class KthLargest:
    """
    Time O(N)  Space O(2N)
    """

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = sorted(nums, reverse=True)[:self.k]

    def add(self, val: int) -> int:
        if len(self.heap) <= self.k:
            self.heap += [val]
            self.heap = sorted(self.heap, reverse=True)[:self.k]
        return self.heap[-1]


# Solution 3
"""
Time O(lgN) Space(M + N)
"""


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.array = sorted(nums)
        self.length = len(nums)

    def add(self, val: int) -> int:
        bisect.insort(self.array, val)
        self.length += 1
        return self.array[self.length - self.k]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
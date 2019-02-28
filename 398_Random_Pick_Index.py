from random import randint
class Solution:
    # Solution 1: O(N) Time O(1) Space
    def __init__(self, nums: List[int]):
        self.cur = nums

    def pick(self, target: int) -> int:
        """
        利用蓄水池采样算法实现   
        """
        index = None
        count = 0
        cur = self.cur
        for i in range(len(cur)):
            if cur[i] == target:
                if randint(0, count) == 0:
                    index = i
                count += 1
        return index 
    


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

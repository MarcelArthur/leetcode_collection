#!python3
class Solution:
    # Time O(N) Space O(1)
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res_one = sum(nums[:k])
        res = res_one
        for i in range(k, len(nums)):
            res_one = res_one - nums[i - k] + nums[i]
            res = max(res, res_one)
        return res/k
            
# 99% 
class Solution:
    # Time O(N) Space O(1)
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res_one = sum(nums[:k])
        res = res_one
        for i in range(k, len(nums)):
            res_one += (nums[i] - nums[i-k])
            res = max(res, res_one)
        return res/k

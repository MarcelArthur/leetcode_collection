#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return 
        res = []
        bigger = deque()
        for i, n in enumerate(nums):
            while bigger and nums[bigger[-1]] < n:
                bigger.pop()

            bigger += [i]

            if i - bigger[0] >= k:
                bigger.popleft()
            
            if i + 1 >= k:
                res.append(nums[bigger[0]])
        return res
        
# @lc code=end


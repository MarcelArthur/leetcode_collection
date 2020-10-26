#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0 
        # B = nums[::-1]
        # for i in range(1, len(nums)):
        #     nums[i] *= nums[i-1] or 1
        #     B[i] *= B[i-1] or 1
        # return max(B + nums)


        maxi, mini, res = 1, 1, float("-inf")
        for n in nums:
            a, b = mini * n, maxi * n
            mini = min(a, b, n)
            maxi = max(a, b, n)
            res = max(res, maxi)
        return res 
# @lc code=end


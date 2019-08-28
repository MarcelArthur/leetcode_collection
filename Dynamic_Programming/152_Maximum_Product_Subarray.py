class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return nums
        # if len(nums) < 2:
        #     return nums[0]
        # dp = [-9999 for x in nums]
        # dp[0], dp[1] = nums[0], nums[1]
        '''
        考虑到负数情况，所以需要保留最小值~
        '''
        mar = nums[0]
        mir = nums[0]
        MAX = nums[0]
        for i in range(1, len(nums)):
            mar, mir = max(nums[i], nums[i] * mar, nums[i] * mir), min(nums[i], nums[i] * mar, nums[i] * mir)
            MAX = max(MAX, mar)
        return MAX

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        B = A[::-1]
        for i in range(1, len(nums)):
            A[i] *= A[i-1] or 1
            B[i] *= B[i-1] or 1
        return max(A + B)

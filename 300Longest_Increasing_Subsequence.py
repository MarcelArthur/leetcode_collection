class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        Solution 1:动态规划方程 递推公式为查找左侧所有符合条件的结果并且更新。
        时间复杂度O(N^2)
        '''
        # if not nums:
        #     return 0
        # MAX = 0
        # m = len(nums)
        # dp = [1] * m
        # for i in range(m):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[j] + 1, dp[i])
        #     MAX = max(MAX, dp[i])
        # return MAX
        '''
        时间复杂度O(N*logN)
        '''
        
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = int((i + j) / 2)
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(i + 1, size)
        return size

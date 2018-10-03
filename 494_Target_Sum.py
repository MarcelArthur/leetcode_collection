class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        '''
        1 DFS暴力搜索 递归过深 失败
        '''
#         self.__count = 0
#         def dfs(nums, depth, sums, S):
#             if depth == len(nums):
#                 if sums == S:
#                     self.__count += 1
#                 return
#             dfs(nums, depth + 1, sums + nums[depth], S)
#             dfs(nums, depth - 1, sums - nums[depth], S)
            
#         dfs(nums, 0, 0, S)
#         return self.__count

        '''
        2 动态规划转化为数学问题(详情见大神描述)
        Markdonw预定
        url: https://leetcode.com/problems/target-sum/discuss/97334/java-15-ms-c-3-ms-ons-iterative-dp-solution-using-subset-sum-with-explanation
        
        '''
                
        __sums = sum(nums)
        if __sums < S or (__sums + S) % 2 > 0:
            return 0
        target = (__sums  + S) >> 1
        return self.substream(nums, target)
    def substream(self, nums, target):
        dp = [0 for x in range(target + 1)]
        dp[0] = 1
        for n in nums:
            for i in range(target, n - 1, -1):
                dp[i] += dp[i - n]
        return dp[target]   

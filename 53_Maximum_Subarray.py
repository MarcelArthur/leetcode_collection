class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        算法分析参考自https://blog.csdn.net/zgljl2012/article/details/72085674
        考虑到思想接近动规
        '''
        __sum = 0
        __max = -2 ** 31
        for i in range(len(nums)):
            __sum = nums[i] + (0 if __sum < 0 else __sum) 
            __max = __sum if __sum > __max else __max
        return __max
        
        
        '''
        Solution 2:
        url: https://leetcode.com/problems/maximum-subarray/discuss/20396/Easy-Python-Way
        分治/动规思想
        取相邻的前一个元素判断如果大于0则，对累加并更新数组元素值(可以理解为阶段求和，当元素累加小于0时放弃前一阶段的值，持续累加有效值，更新数组，知道所有值遍历完成，某一阶段的最大值也在更新后的数组中，直接对齐取极大值即可)
        '''
        
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)

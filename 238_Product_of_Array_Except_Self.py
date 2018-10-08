class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        '''
        Solution 1:
        时间复杂度O(N),空间复杂度O(1),AC 97%
        实际上类似于存水问题
        分别从左右两边各扫一次记录目标值，左侧值加入列表，右侧值更新列表，直到除自己以外的所有值完成更新即可认为所有值已经更新到符合要求的结果
        '''
        
        p = 1
        n = len(nums)
        out = []
        for i in range(n):
            out.append(p)
            p *= nums[i] 
        p = 1
        for j in range(n-1, -1, -1):
            out[j] *= p
            p *= nums[j] 
        return out
            

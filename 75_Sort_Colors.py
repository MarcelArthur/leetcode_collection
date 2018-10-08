class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        '''
        时间复杂度O(2N),空间复杂度O(N)
        计数排序
        观察可得最大元素不超过2，只是增加各种元素的顺序,所以需要处理下元素列表过少但是单个元素值比较大的情况，这里统一根据规律设置成最小计数列表长度为4
        1 计数列表记录出现有效值的数量，对每个元素作为索引数进行计数。
        2 根据计数列表的索引和数量再次遍历覆盖原有数组即可获得有序列表
        '''
        length = len(nums)
        dp = [0] * (max(nums) + 1 if length < 3 else length)
        
        # step 1: 对数组内元素进行计数
        for i in range(length):
            dp[nums[i]] += 1
        
        # step 2: 对计数结果处理还原顺序覆盖数组
        res_index = 0
        for j in range(len(dp)):
            if dp[j] == 0: continue
            for n in range(dp[j]):
                nums[res_index] = j
                res_index += 1
        
                    
    
        

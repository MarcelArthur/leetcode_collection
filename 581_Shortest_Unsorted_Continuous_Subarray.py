class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Solution 1:分别以两个方向来找到beg 和 end
        # 记录初始化的beg和end,分别搜索更新max和end的信息和min和beg的信息,查找最短非升序子序列的起始和终止Index
        n = len(nums)
        beg = -1
        end = -2
        
        minn = nums[-1]
        maxn = nums[0]
        
        for i in range(len(nums)):
            maxn = max(maxn, nums[i])
            minn = min(minn, nums[n - 1 - i])
            
            if nums[i] < maxn:
                end = i
            if nums[n - 1 - i] > minn:
                beg = n - 1 - i
            
        return end - beg + 1
        
        

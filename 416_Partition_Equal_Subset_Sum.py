class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Solution 1:
        # 深度遍历dfs获得所有子树的遍历结果查找答案
        # Sum=sum(nums)
        # if Sum%2==1:
        #     return False
        # target=Sum/2  #find subset sum is target
        # nums.sort(reverse=True)
        # def dfs(i,val):
        #     if val==0:
        #         return True
        #     if i==len(nums) or val<0 or nums[i]>val:
        #         return False
        #     return dfs(i+1,val-nums[i]) or dfs(i+1,val)
        # return dfs(0,target)
        # Solution 2:
        # 利用数组dp[i]记录和为i的子数组是否存在，初始令dp[0] = 1
        # for num in nums:
        #     for i in range(sum(nums) - num + 1):
        #         if dp[i]: dp[i + num] = 1
        # 使用动规DP查找对应的函数结果值, 首先确认背包总和为偶数，否则没有相等的两个子集。之后利用DP思想加入背包所有可能的结果，判断是否有可二分切分的内容在背包中，如果有则说明可以分为两个相等的子集。
        sums=sum(nums)
        if sums & 1:
            return False
        nset = set([0])
        for i in nums:
            for j in nset.copy():
                nset.add(i + j)
        return sums/2 in nset
    
        # Solution 3:
        # 利用bitset进行处理问题
        # pass
            

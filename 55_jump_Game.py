class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        '''
        深度搜索
        不知道为什么不能判断出结果= =orz
        Solution 1
        '''
    #     self.status = False
    #     self.DFS(nums, 0, self.status)
    #     return self.status
    #     '''
    #     DP
    #     '''
    # def DFS(self, nums, index, status):
    #     if index == len(nums) - 1:
    #         # print(index)
    #         self.status = True
    #     if index > len(nums) - 1 or nums[index] == 0:
    #         return
    #     for i in range(1, nums[index] + 1):
    #         index += i
    #         self.DFS(nums, index, status)
    
        '''
        Solution 2:
        这个题目挺有意思
        其实可以观察到 左边所有的跳跃长度的上线是由(位置 + 距离)共同组成的,那么只需要判断这个距离的上限是不是在某一时刻没有达到位置的坐标即可(即无法跳跃到某一位置则认为无法跳跃到最后)，那么就可以在O(N)复杂度时间内判断最后是否能够达到last index。
        '''
        max_rec = 0
        for i, v in enumerate(nums):
            if i > max_rec:
                return False
            max_rec = max(max_rec, i + v)
        return True
        
        

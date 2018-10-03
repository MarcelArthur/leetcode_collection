class Solution:
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        一次AC！ 撒花 100% 其实也没说的基本上就是根据题意只做标记叠加即可，特别判断的是第一次两元素之间的差值可能是负数/正数，这里需要特殊判断一次以外，其他情况就是根据原有标记记录最长子序列长度，因为是剔除式的记录，所以保留下来的一定是一组子序列长度。
        '''
        if not nums:
            return 0
        d = None
        n = 0
        result = 1
        while n < len(nums) - 1:
            if (d == None or d) and nums[n] < nums[n + 1]:
                result += 1
                d = 0
            elif (d == None or not d) and nums[n] > nums[n + 1]:
                result += 1
                d = 1
            
            n += 1
        return result

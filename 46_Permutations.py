#from itertools import permutations
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        '''
        一行代码....
        '''
        # return [list(x) for x in list(permutations(nums, len(nums)))]
        '''
        正常版
        深度搜索
        Solutions 1:
        '''
        
        n = len(nums)
        if n < 1: return [[]]
        
        def DFS(nums, level, current, res):
            if level == n: 
                res.append(current)
            else:
                for num in nums:
                    if num not in current: # I wonder if this will be even faster with a set
                        DFS(nums, level+1, current + [num], res)
        
        res = []
        DFS(nums,0,[],res)
        return res

from itertools import combinations
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        '''
        快捷方便的组合包combinations
        '''
        if not nums:
            return []
        res = []
        for i in range(len(nums) + 1):
            res += list(combinations(nums, i))
            
        return res
    
        '''
        Solution 1:
        深度搜索
        逐层查找,判断是否满足所需要的长度(1,2,3,...)直到所有长度全部满足则认为所有的结果已经遍历完成
        url: https://leetcode.com/problems/subsets/discuss/177138/Easy-Python-Solution
        '''
        res = [[]]
        def find(tag,tags,length):
            if len(tags)<length:
                for i in range(len(tag)):
                    find(tag[i+1:],tags+[tag[i]],length)
            else:
                res.append(tags)
        for i in range(len(nums)):
            find(nums,[],i+1)
        return res
        

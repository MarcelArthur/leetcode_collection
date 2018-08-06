# !python3
'''
通用算法只能有26%的AC
目前来看比较靠前的一种算法解决方案
'''
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        res = {}
        stack = []
        for i in nums:
            while stack != [] and stack[-1] < i:
                res[stack.pop()] = i
            stack.append(i)
        nxt = []
        for i in findNums:
            nxt.append(res.get(i, -1))
        return(nxt)

# python3

'''
低效算法 没有通过AC
'''
from functools import reduce
import copy


class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def combin(nums, length):
            v = 0
            L = []
            while len(nums) != length-1:
                L.append(nums[:length:])
                del nums[0]
            return L
        def combinations_list(list_dev):
            G = []
            v = len(list_dev)
            for i in range(1, v+1):
                G.extend(combin(copy.copy(list_dev), i))
            return G
        def mul(L):
            return reduce(lambda x, y: x * y, L)
        count = 0
        for i in combinations_list(nums):
            if mul(i) < k:
                count += 1
        else:
            return count


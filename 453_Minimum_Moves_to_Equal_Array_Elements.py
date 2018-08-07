# !python3
'''
解题思路:刚刚开始的是按照个给出的解题线索思考，那么每次增加的数为(数组长度 - 1)，计算达到所有数为一个值的时候增加的数目和，但是情况
比较多，而且分析起来肯定是要超过OJ时长的，所以转变思路考虑转变为的所有值的目前所有值的最小值(和转变为最大值相同的思路)，不过这里有明确的下限
之后求所有值和最小值的差值并且求和就能得到结果
'''


class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_min = max(nums)
        res = 0
        for i in nums:
            num_min = min(num_min, i)
        for i in nums:
            res += i - num_min
        return res

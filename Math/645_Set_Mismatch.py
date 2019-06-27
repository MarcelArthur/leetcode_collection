#!python3
import collections
from typing import List


class Solution:
    # 普通解法 利用Counter记录所有出现过的值的次数
    def findErrorNums(self, nums: List[int]) -> List[int]:
        c = collections.Counter(nums)
        dup = [k for k, v in c.items() if v == 2][0]
        o = (len(nums) * (len(nums) + 1) / 2) - sum(nums)
        return [dup, int(o + dup)]

    # one-liner Python
    # https://leetcode.com/problems/set-mismatch/discuss/105558/Oneliner-Python
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # 1. 52ms
        return [sum(nums) - sum(set(nums)), sum(range(1, len(nums) + 1)) - sum(set(nums))]

    def findErrorNums(self, nums: List[int]) -> List[int]:
        # 2. 56ms 竟然比range慢(迭代器)
        return [sum(nums) - sum(set(nums), (len(nums) - (1 + len(nums)))) // 2 - sum(set(nums))]

#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        current = float("inf")
        res = 0
        for p in prices:
            if p < current:
                current = p
            res = max(res, p - current)
        return res
# @lc code=end


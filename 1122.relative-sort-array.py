#
# @lc app=leetcode id=1122 lang=python3
#
# [1122] Relative Sort Array
#

# @lc code=start
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        k = {v:i for i, v in enumerate(arr2)}
        return sorted(arr1, key=lambda i: k.get(i, 1000+i))
# @lc code=end


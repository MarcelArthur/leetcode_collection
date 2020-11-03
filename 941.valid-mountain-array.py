#
# @lc app=leetcode id=941 lang=python3
#
# [941] Valid Mountain Array
#

# @lc code=start
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        i, j, n = 0, len(A) - 1, len(A)
        while i + 1 < n and A[i] < A[i+1]:
            i += 1
        while j > 0 and A[j-1] > A[j]:
            j -= 1
        return 0 < i == j < n - 1
# @lc code=end


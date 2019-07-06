#!python3
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        # https://leetcode.com/problems/largest-perimeter-triangle/discuss/286597/Python3%3A-faster-than-97
        # Space O(1) Time(lgN + N)
        A.sort(reverse=True)
        for i in range(len(A) - 2):
            if A[i] < A[i + 1] + A[i + 2]:
                return A[i] + A[i+1] + A[i+2]
        return 0

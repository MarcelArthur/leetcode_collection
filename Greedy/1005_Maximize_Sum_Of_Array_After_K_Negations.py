#!python3

class Solution:
    # https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/discuss/252254/C%2B%2BPython-Sort
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()
        i = 0
        while i < len(A) and i < K and A[i] < 0:
            A[i] = -A[i]
            i += 1
        return sum(A) - (K-i) % 2 * min(A) * 2
    
# 思路清晰的的代码
class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A, i = sorted(A), 0
        while A[i] <= 0 and K > 0:
            A[i] = -A[i]
            i += 1
            K -= 1
        
        if K == 0 or 0 in A or K % 2 == 0:
            return sum(A)
        else:
            return sum(A) - min(A) * 2            
        

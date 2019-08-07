#!python3
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        status = -1
        for i in range(len(A) - 1):
            cur_status = -1
            if A[i] > A[i+1]:
                cur_status = 0
            elif A[i] < A[i+1]:
                cur_status = 1
            if cur_status == -1:
                continue
            if status == -1:
                status = cur_status
            elif status != cur_status:
                return False
        return True
            

# One liner
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        return A == sorted(A) or A == sorted(A, reverse=True)
    
# one pass
class Solution(object):
    def isMonotonic(self, A):
        increasing = decreasing = True
        
        for i in range(len(A) - 1):
            if A[i] > A[i+1]:
                increasing = False
            elif A[i] < A[i+1]:
                decreasing = False
        return increasing or decreasing

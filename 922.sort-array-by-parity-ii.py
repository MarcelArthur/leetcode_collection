#
# @lc app=leetcode id=922 lang=python3
#
# [922] Sort Array By Parity II
#

# @lc code=start
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        if not A:
            return A
        # odd, even = [], []
        # res = []

        # for num in A:
        #     if num % 2 == 0:
        #         even.append(num)
        #     else:
        #         odd.append(num) 

        # for _ in range(len(A)//2):
        #     res.append(even.pop())
        #     res.append(odd.pop())
        
        # return res
        i, j, sz = 0, 1, len(A)

        while i < sz and j < sz:
            if  A[i] % 2 != 0:
                A[i], A[j] = A[j], A[i]
                j += 2
            else:
                i += 2
                
                
        return A
# @lc code=end


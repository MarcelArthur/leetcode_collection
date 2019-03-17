# https://leetcode.com/problems/2-keys-keyboard/
class Solution:
    def minSteps(self, n: int) -> int:
        ans = 0
        d = 2
        while n > 1:
            if n % d == 0:
                n = n/d
                ans += d
            else:
                d += 1
        return ans
    
    # Solution 1:
#     def minSteps(self, n:int) -> int:
        
#         def recur(already, copied):
#             if already == n:
#                 return 0
#             if already > n:
#                 return n
            
#             if (already, copied) not in momo:
#                 choicePaste = 1 + recur(already + copied, copied)
#                 choiceCopy = 2 + recur(already * 2, already)
#                 momo[(already, copied)] = min(choicePaste, choiceCopy)
#             return momo[(already, copied)]
        
#         momo = {}
#         if n == 1:return 0
#         return 1 + recur(1, 1)

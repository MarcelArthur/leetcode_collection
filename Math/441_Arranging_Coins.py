#!python3
import math
# 漂亮的公式推导 
# n = (x + 1) * x / 2
# x² + x = 2n
# x² + x + 1/4 - 1/4 = 2n
# (x + 1/2)² = 2n + 1 / 4
# (x + 1/2)² = (8n + 1) / 4
# x + 1/2 = sqrt(8n + 1) / 2
# x = (sqrt(8n + 1) / 2) - (1 / 2)
# x = (sqrt(8n + 1) - 1) / 2
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((math.sqrt(8 * n + 1) - 1)/2)

# 全场最佳 binary search
class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n < 1:
            return 0
        
        start = 0
        back = n
        mid = 0
        while start <= back:
            mid = (start + back) // 2
            r = (mid**2 + mid) >> 1
            if r > n:
                back = mid - 1
            elif r < n:
                start = mid + 1
            else:
                return mid
        if (mid ** 2 + mid) >> 1 > n:
            mid -= 1
        return mid
            
            

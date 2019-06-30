#!python3
class Solution:
    # def isPerfectSquare(self, num: int) -> bool:
    #     # Solution Bufce 
    #     if num < 2:
    #         return True
    #     for i in range(2, num//2+1):
    #         if i*i == num:
    #             return True
    #         elif i * i > num:
    #             return False
    #     return False
    
    def isPerfectSquare(self, num: int) -> bool:
        # Binary search
        if num <= 4:
            if num in [1, 4]:
                return True
            else:
                return False
        l = 1
        r = num
        while l <= r:
            mid = (l + r)//2
            res = mid * mid
            if res > num:
                r = mid - 1
            elif res < num:
                l = mid + 1
            else:
                return True
        return False

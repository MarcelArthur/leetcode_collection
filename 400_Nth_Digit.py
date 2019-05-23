#!python3


class Solution:
    def findNthDigit(self, n: int) -> int:
        """
        levels:
            nums    width    count
            1-9       1       9
            10-99     2       90
            100-999   3       900
            ...
        """ 
        w, c = 1, 9 # width and count numbers (of each levels)
        while n > w*c:
            n -= w*c
            w += 1
            c *= 10
        nums, d = (c/9) + (n-1)/w, (n-1)%w   # c/9 equals 10**w, means the base number
        return int(str(nums)[d])
        
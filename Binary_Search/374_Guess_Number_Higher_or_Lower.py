#!python3
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # binary search
        # Time O(nlogn) Space O(1)
        start = 1
        back = n
        
        while start <= back:
            mid = (start + back) // 2
            val = guess(mid)
            if val == 0:
                return mid
            elif val > 0:
                start = mid + 1
            else:
                back = mid - 1
        return -1

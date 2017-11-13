# -*- coding:utf-8 -*-
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            x = -x
            if x == int(str(x)[::-1]):
                return True
            else:
                return False
        else:
            if x == int(str(x)[::-1]):
                return True
            else:
                return False


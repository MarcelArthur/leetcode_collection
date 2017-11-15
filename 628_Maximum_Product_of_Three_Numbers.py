# python3
'''
description: 维护一个最大堆和最小堆，遍历一遍数组，持续更新最大堆和最小堆的值，从而得到一个2个元素的最小堆和3个元素的最大堆.
时间复杂度O(n), 空间复杂度O(1)

Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:
Input: [1,2,3]
Output: 6
Example 2:
Input: [1,2,3,4]
Output: 24
Note:
The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
'''

import sys
class Soluction:
    def maximumProduct(self, nums):
        min1, min2 = sys.maxsize, sys.maxsize
        max1, max2, max3 = -sys.maxsize, -sys.maxsize, -sys.maxsize
        for i in nums:
            if i < min1:
                min2 = min1
                min1 = i
            elif i < min2:
                min1 = i
            if i > max1:
                max3 = max2
                max2 = max1
                max1 = i
            elif i > max2:
                max3 = max2
                max2 = i
            elif i > max3:
                max3 = i
        return max(min1*min2* max1, max1*max2*max3)
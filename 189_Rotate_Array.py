#!python3
from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Solution 1: 循环插入 AC 时间复杂度快20%, 空间复杂度少于 20%
        for _ in range(k):
            nums.insert(0, nums.pop())

            # Solution 2:  AC time faster than 27.05%, memory less than 5.01%
        l = len(nums)
        nums[:l - k] = reversed(nums[:l - k])
        nums[l - k:] = reversed(nums[l - k:])
        nums[:] = reversed(nums)

        # Solution 3: AC time faster than 97.34%, memory less than 86%, 时间复杂度O(N), 空间复杂度O(1)
        """
        solution explain: 
        整体思想: 三次反转即可得到最终结果(不使用额外空间情况下)
        1.rev函数对数组依次反转，使用首尾一一对应的元素交换
        2.注意k>n的情况，当k=n时不会再继续交换，所以需要对k取模得到余数
        """
        n = len(nums)
        k = k % n

        def rev(start, end, s):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1

        rev(0, n - 1, nums)
        rev(0, k - 1, nums)
        rev(k, n - 1, nums)




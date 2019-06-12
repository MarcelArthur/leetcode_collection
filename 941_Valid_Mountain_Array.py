#!python3
"""
Given an array A of integers, return true if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[B.length - 1]


Example 1:

Input: [2,1]
Output: false
Example 2:

Input: [3,5,5]
Output: false
Example 3:

Input: [0,3,2,1]
Output: true

Note:

0 <= A.length <= 10000
0 <= A[i] <= 10000
"""
from typing import List


class Solution:

    def validMountainArray(self, A: List[int]) -> bool:
        # 一次循环拆成两次处理 Time O(N)
        if len(A) < 3 or A[0] >= A[1]:
            return False
        peak = 0
        index = 0
        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                peak = A[i]
                index = i
                break
            if A[i] == A[i + 1]:
                return False
        for i in range(index + 1, len(A) - 1):
            if A[i] <= A[i + 1] or A[i] > peak:
                return False
        return True

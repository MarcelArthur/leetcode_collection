#!python3
"""
Given two integers A and B, return any string S such that:

S has length A + B and contains exactly A 'a' letters, and exactly B 'b' letters;
The substring 'aaa' does not occur in S;
The substring 'bbb' does not occur in S.
Example 1:

Input: A = 1, B = 2
Output: "abb"
Explanation: "abb", "bab" and "bba" are all correct answers.
Example 2:

Input: A = 4, B = 1
Output: "aabaa"


Note:

0 <= A <= 100
0 <= B <= 100
It is guaranteed such an S exists for the given A and B.

"""


class Solution:
    """
    Solution explain:
    观察规律:
           1. 当A和B都数量都小于等于2时，返回任意组合都字符串都可以
           2. 通常当A大于B时, 默认最大字符串数量m为A的数量, 否则为B的数量
           3. 初始位置为2, 每次改变一对ab(即两个b一个a，或者两个a一个b)
    时间复杂度:
        最多字符串长度为m+n, 故时间复杂度为O(m + n)
    空间复杂度:
        原因同上，O(m + n)
    """
    def strWithout3a3b(self, A: int, B: int) -> str:
        if A < 3 and B < 3:
            return A * 'a' + B * 'b'
        m, n = 'a', 'b'
        flag = B
        if A < B:
            m, n = 'b', 'a'
            flag = A
        start = 2
        tmp = [m] * (A + B)
        while flag:
            for i in range(start, A + B, 3):
                if i > -1:
                    flag -= 1
                    tmp[i] = n
                if flag == 0:
                    break
            start -= 1
        return "".join(tmp)



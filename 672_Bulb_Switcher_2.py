#!python3
"""
关灯问题2
There is a room with n lights which are turned on initially and 4 buttons on the wall. After performing exactly m unknown operations towards buttons, you need to return how many different kinds of status of the n lights could be.

Suppose n lights are labeled as number [1, 2, 3 ..., n], function of these 4 buttons are given below:

Flip all the lights.
Flip lights with even numbers.
Flip lights with odd numbers.
Flip lights with (3k + 1) numbers, k = 0, 1, 2, ...


Question Explain:

观察规律:

- 当m和n其中有任意一个数是0时，返回1

- 当n = 1时

只有两种情况，0和1

- 当n = 2时，

这时候要看m的次数，如果m = 1，那么有三种状态 00，01，10

当m > 1时，那么有四种状态，00，01，10，11

- 当m = 1时，

此时n至少为3，那么我们有四种状态，000，010，101，011

- 当m = 2时，

此时n至少为3，我们有七种状态：111，101，010，100，000，001，110

- 当m > 2时，

此时n至少为3，我们有八种状态：111，101，010，100，000，001，110，011


"""


class Solution:
    def flipLights(self, n: int, m: int) -> int:
        if n == 0 or m == 0:
            return 1
        if n == 1:
            return 2
        if n == 2:
            return 3 if m == 1 else 4
        if m == 1:
            return 4
        return 7 if m == 2 else 8

    # Solution 2:
    # StefanPochmann 大神的解法，然而并没有解释为什么可以这么做
    # https://www.cnblogs.com/grandyang/p/7595595.html
    def filpLights(self, n: int, m: int) -> int:
        n = min(n, 3)
        return min(1 << n, 1 + m*n)


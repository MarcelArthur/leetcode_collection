#!python3

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        res = set()
        idx = 0
        while idx * idx <= c:
            res.add(idx * idx)
            idx += 1

        for v in res:
            if (c - v) in res:
                return True
        return False

    # Solution 基于费马大定理衍生出来的推广公式: 某个数字的4k+3的质数因子的个数均为偶数时，可以拆分为两个平方数之和
    def judgeSquareSum(self, c: int) -> bool:
        i = 2
        while i * i <= c:
            if c % i != 0:
                i += 1
                continue
            count = 0
            while c % i == 0:
                count += 1
                c /= i
            if i % 4 == 3 and count % 2 != 0:
                return False
            i += 1
        return c % 4 != 3

    # Solution https://leetcode.com/problems/sum-of-square-numbers/solution/
    # 确认结果是否为整数判断
    def judgeSquareSum(self, c: int) -> bool:
        return any(int((c - i * i) ** 0.5) ** 2 == (c - i * i) for i in range(int(c ** 0.5) + 1))

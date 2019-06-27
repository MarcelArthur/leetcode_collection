#!Python3
from itertools import product
from typing import List

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        # Solution 层次遍历收集结果
        s = set()
        stack = [(0, 0)]
        while stack:
            i, j = stack.pop(0)
            t = x ** i + y ** j
            if t <= bound:
                s.add(t)
                if x > 1:
                    stack.append((i + 1, j))
                if y > 1:
                    stack.append((i, j + 1))
        return list(s)

    # Solution 2
    def exp_below_bound(self, n: int, bound: int) -> List[int]:
        ns = [1]
        i = 0
        if n == 1:
            return ns

        while n ** i < bound:
            exp = n ** i
            ns.append(exp)
            i += 1
        return ns

    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:

        nx = self.exp_below_bound(x, bound)
        ny = self.exp_below_bound(y, bound)

        return list(set([x + y for x, y in product(nx, ny) if x + y <= bound]))


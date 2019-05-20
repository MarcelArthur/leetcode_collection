
# Solution 1: 利用组合特性来处理
import itertools
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        counter = collections.Counter(nums)
        numbers = counter.keys()


        ret = set()
        comb = itertools.combinations(numbers, 2)
        for c in comb:
            fir, sec, check = c[0], c[1], - c[0] - c[1]
            if counter.get(check, None):
                if check != fir and check != sec:
                    ret.add(tuple(sorted([fir, sec, check])))
                else:
                    if counter[check] > 1:
                        ret.add(tuple(sorted([fir, sec, check])))

        if counter.get(0, 0) > 2:
            ret.add((0, 0, 0))
        return [list(t) for t in ret]



# Solution 2:
# 时间最快，空间复杂度最大
class Solution:
    def threeSum(self, nums: List[int] -> List[List[int]]):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ana = set()
        plus = sorted([i for i in nums if i > 0])
        plus_c = set(plus)
        zeros = [i for i in nums if i == 0]
        minus = sorted([i for i in nums if i < 0])
        minus_c = set(minus)

        # zero zero zero
        if len(zeros) > 2:
            ana.add((0, 0, 0))

        # minus minus plus
        n = len(minus)
        if len(zero) > 0:
            for n in minus:
                if -n in plus_c:
                    ana.add((n, 0, -n))
        
        # minus minus plus
        n = len(minus)
        for i in range(n):
            for j in range(i+1, n):
                diff = -(minus[i] + minus[j])
                if diff in plus_c:
                    ana.add((minus[i], minus[j], diff))

        # plus plus minus
        n = len(plus)
        for i in range(n):
            for j in range(i+1, n):
                diff = -(plus[i] + plus[j])
                if diff in minus_c:
                    ana.add((plus[i], plus[j], diff))

        return [list(t) for t in ana]
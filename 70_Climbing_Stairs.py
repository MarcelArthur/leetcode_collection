class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Solution 1: 时间复杂度O(N), 空间复杂度O(N)
        if not n:
            return n
        # 动态规划 实际上是斐波那契应用问题~ 
        one, two = 1, 2
        for i in range(3, n + 1):
            one, two = two, one + two
        return (n if n <= 2 else two)
        # Solution 2:
        result = []
        for i in range(n + 1):
            if i <= 2:
                result.append(i)
            else:
                result.append(result[i-1], result[i-2])
        return result[-1]


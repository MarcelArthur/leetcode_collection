class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return n
        # 动态规划 实际上是斐波那契应用问题~ 
        one, two = 1, 2
        for i in range(3, n + 1):
            one, two = two, one + two
        return (n if n <= 2 else two)

class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 递归算法
        if n < 5:
            return 0
        elif n < 10:
            return 1
        
        return (n // 5 + self.trailingZeroes(n//5))
        # Solution 1: 判断是否为5的阶乘结果
        # 非递归算法
        c = 0
        while n > 0:
            n //= 5
            c += n
        return c
        

class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Solution 1:递归实现
        if n == 1:
            return True
        if n == 4:
            return False
        happy_number = [int(x) for x in list(str(n))]
        f = lambda x: x**2
        happy_one = sum(list(map(f, happy_number)))
        return self.isHappy(happy_one)
        # Solution 2: 利用一个set集合判断无限循环是否出现过数字,若未出现则加入集合，出现则判断是否为1或4。1为True, 4为False
        
        

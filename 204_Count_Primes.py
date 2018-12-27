class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Solution 1: 素数的倍数为非素数,更新列表内的所有非素数标记。优化方案暂无。时间复杂度O(N + m)
        # if n <= 2:
        #     return 0
        # isPrimes = [1] * n
        # for i in range(2, n):
        #     if isPrimes[i] == 1:
        #         j = 2 * i
        #         while j < n:
        #             isPrimes[j] = 0
        #             j += i
        # return sum(isPrimes) - 2
        # Solution 2:https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
        if n <= 2:
            return 0
        isPrimes = [1] * n
        isPrimes[0] = isPrimes[1] = 0
        for i in range(2, int(n * 0.5) + 1):
            if isPrimes[i] == 1:
                isPrimes[i * i:n:i] = [0] * len(isPrimes[i * i:n:i])
        return sum(isPrimes) 

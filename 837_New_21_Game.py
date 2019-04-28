class Solution(object):
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        if K == 0: return 1
        dp = [1.0] + [0.0] * N
        # Wsum表示(前W个dp之和)/W
        Wsum = 1.0000
        for i in range(1, N + 1):
            dp[i] = Wsum / W
            # 因为当i>=K时，不能再取数，因此后面的概率不能累加
            if i < K: Wsum += dp[i]
            # 因为只需要计算前w个dp之和，所以当i>=W时，减去最前面的dp。
            if 0 <= i - W < K: Wsum -= dp[i - W]
        return sum(dp[K:])

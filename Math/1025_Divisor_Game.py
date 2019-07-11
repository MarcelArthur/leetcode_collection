#!python3
class Solution:
    def divisorGame(self, N: int) -> bool:
        # wow, awesome
        return N % 2 == 0
    
    
        # DP 解法 模拟选择
        dp = [False for x in range(N+1)]
        for i in range(2, N+1):
            for j in range(1, i//2+1):
                if (i % j == 0) and (not dp[i - j]):
                    dp[i] = True
                    break
        return dp[N]

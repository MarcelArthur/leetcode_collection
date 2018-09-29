class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # 1 贪心算法某些时候不能得到全局最优解(即最小实现方案硬币找零的方案)
        # 使用动态规划
        if amount < 0:
            return -1
        dp = [9999 for x in range(amount)]
        
        dp = [0] + dp
            
        for coin in coins:
            for i in range(coin, amount +1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return (-1 if dp[amount] == 9999 else dp[amount])

# 优化
class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # 1 贪心算法某些时候不能得到全局最优解(即最小实现方案硬币找零的方案)
        # 使用动态规划
        if amount < 0:
            return -1
        dp = [9999 for x in range(amount)]

        dp = [0] + dp
        for coin in coins:
            for i in range(coin, amount +1):
                if dp[i - coin] >= dp[i]: continue
                dp[i] = dp[i - coin] + 1

        return (-1 if dp[amount] == 9999 else dp[amount])

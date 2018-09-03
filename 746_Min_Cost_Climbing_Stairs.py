class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]  每一步的花销
        :rtype: int 到达顶点所需要的最终花销
        """
        # DP动态规划，逆推计算公式的方法: 基本的状态转移方程是 dpN = min(dp0 + cost[i - 2], dp1 + cost[i - 1])
        dp0, dp1 = 0, 0
        for n in reversed(cost):
            dp0, dp1 = n + min(dp0, dp1), dp0
        return min(dp0, dp1)





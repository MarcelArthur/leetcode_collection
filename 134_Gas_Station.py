class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # 思路链接: https://www.cnblogs.com/boring09/p/4248482.html
        # Great Solution 1: 基于数学定理
        # 如果一个数组的总和非负，那么一定可以找到一个起始位置，从他开始绕数组一圈，累加和一直都是非负的
        # 求取开始位置只需要关注在哪个为止开始之后到某一位置油耗不满足跑完剩下路程，则应该从j+1位置开始
        start = 0
        remain = 0
        dept = 0
        
        for i in range(len(gas)):
            remain += gas[i] - cost[i]
            if remain < 0:
                dept += remain 
                start = i + 1
                remain = 0
        return (start if remain + dept >= 0 else -1)
    
        # Solution: DP
        # https://leetcode.com/problems/gas-station/discuss/206911/Python-beats-100-with-explanation-and-plots
        n = len(gas)
        dp = [gas[0] - cost[0]]
        for i in range(1, n):
            dp.append(dp[-1] + gas[i] - cost[i])
        if dp[-1] < 0:
            return -1
        return (dp.index(min(dp)) + 1) % n

    
    

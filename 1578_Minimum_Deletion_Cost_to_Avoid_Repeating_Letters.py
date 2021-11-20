# My solution 70% faster 59% less
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        if not cost or len(s) == 1:
            return 0
        stack  = []
        res = 0
        stack.append(cost[0])
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                res += sum(stack) - max(stack)
                stack.clear()
            stack.append(cost[i])
        res += sum(stack) - max(stack)
        return res
# Great explain solution
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        res = 0 
        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                res += min(cost[i-1], cost[i])
                cost[i] = max(cost[i-1], cost[i])
        return res

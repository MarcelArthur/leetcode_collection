class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Solution 1: BFS
        codes = set(['1', '2','3','4','5','6','7','8','9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26'])
        dp = dict()

        def mem(x):
            if x == len(s): return 1
            if x in dp: return dp[x]
            
            if s[x] in codes: # 1-9
                dp[x] = mem(x + 1)
                if x < len(s) - 1 and s[x] + s[x+1] in codes: # 10-26
                        dp[x] += mem(x + 2)          
                return dp[x]
            return 0
        
        return mem(0)
    
        # Solution 2: Dp 时间复杂度O(N)
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i in range(1, len(dp)):
            if s[i-1] != '0':
                dp[i] = dp[i-1]
            if i != 1 and '09' < s[i-2:i] < '27':
                dp[i] += dp[i-2]
        return dp[-1]


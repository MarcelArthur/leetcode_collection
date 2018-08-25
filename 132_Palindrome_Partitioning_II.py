# Hard
class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 回溯 or O(N) 遍历
        # 回溯过程中还要进行归并，将符合条件的回文串归并在一起处理，实现最小分割的方法
        # 动态规划 判断i和j之间的临近子字符串是不是也是回文串， 提前处理dp[i]回文串个数 - 1, 再通过dp动态规划获得结果，即可得到分割次数         
        slen = len(s)
        dp = [0 for x in range(slen + 1)]
        for i in range(slen + 1):
            dp[i] = slen - i - 1
        
        P = [[False for x in range(slen)] for y in range(slen)]
        
        for i in range(slen - 1, -1, -1):
            for j in range(i, slen):
                if s[i] == s[j] and ((j - i <= 1) or (P[i + 1][j - 1])):
                    P[i][j] = True
                    dp[i] = min(dp[i], dp[j + 1] + 1)
        
        return dp[0]


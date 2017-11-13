# -*- coding:utf-8 -*-


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        doc:这里设计一个table,其中每一个格子对应相应的对应关系， 可以通过对于特殊字符前后的判断得到对应位置是否可以继续判断
        dp = [[None for x in range(n+1) for j in range(m+1)]]
        +-----------+
        |           |
        +-----------+

        """
        n, m = len(p), len(s)
        dp = [[None for x in range(n+1)] for j in range(m+1)]
        dp[0][0] = True
        for i in range(1, m+1):
            dp[i][0] = False
        for j in range(1, n+1):
            dp[0][j] = j > 1 and '*' == p[j-1] and dp[0][j-2]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] or (s[i - 1] == p[j - 2] or p[j - 2] == '.') and dp[i - 1][j]
                else:
                    dp[i][j] = (p[j - 1] == '.' or s[i - 1] == p[j - 1]) and dp[i - 1][j - 1]

        return dp[m][n]

if __name__ == '__main__':
    Ar = Solution()
    print(Ar.isMatch('aaa', 'a*'))
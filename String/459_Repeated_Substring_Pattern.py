#!python3
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # Solution 重复判断
        if not s:
            return False
        sub = s + s
        return sub[1:-1].find(s) != -1


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # Solution Space O(M) Time O(N) 思路来自同1方法，必然有重复字符串在不完整的字符串拼接中
        if not s:
            return False
        double = s + s
        for i in range(1, len(double) - len(s)):
            if double[i:i + len(s)] == s:
                return True
        return False


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # Solution 思路同1方法 22%
        if not s:
            return False
        for i in range(len(s) // 2 + 1):
            pattern = s[:i]
            if pattern and pattern * (len(s) // len(pattern)) == s:
                return True
        return False


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # Solution KMP算法 Time O(N) Space O(N)  速度是真慢(Python背锅)
        n = len(s)
        dp = [0 for x in range(n + 1)]
        dp[0] = -1
        i, j = 0, -1
        while i < n:
            if j == -1 or s[i] == s[j]:
                i += 1
                j += 1
                dp[i] = j
            else:
                j = dp[j]
        return all((dp[n], dp[n] % (n - dp[n]) == 0))
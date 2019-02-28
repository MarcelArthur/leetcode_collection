class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Solution 1: 朴素算法 略 时间复杂度O(N^2)
        # Solution 2:
        # DP/奇数偶数字符串回文子串比对  O(n^2)处理
        # Manacher 算法 时间复杂度 O(N)处理, 空间复杂度O(1)
        # 1 字符串预处理 2 马拉车算法 快速遍历到字符串子串的结果 
        sc = '#' + '#'.join(s) + '#'
        n = len(sc)
        p = [0] * n
        _id = mx = res = 0
        for i in range(1, n - 1):
            if (mx > i):
                p[i] = min(mx - i, p[2 * _id - i])
            while i+p[i]+1 < n and i-p[i]-1 >=0 and sc[i+p[i]+1] == sc[i-p[i]-1]:
                p[i] += 1
            if (i + p[i] > mx):
                _id = i
                mx = i + p[i]
            res += int((p[i] + 1) / 2)
        return res

                
        
        
        
        
        

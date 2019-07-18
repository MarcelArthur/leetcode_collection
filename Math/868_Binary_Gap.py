#!python3
class Solution:
    def binaryGap(self, N: int) -> int:
        # 低效但是有用
        pre = res = 0
        for i, v in enumerate(bin(N)[2:]):
            if int(v) == 1:
                res = max(res, i - pre)
                pre = i
        return res
    
class Solution:
    def binaryGap(self, N: int) -> int:
        """
        Solution
        """
        # NB 的 one line 解法
        return max(len(c) for c in bin(N)[2:].strip('0').split('1')) + 1 if N & (N-1) else 0

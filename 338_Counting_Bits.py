class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        '''
        位运算
        观察可得
        偶数末尾必定为0, 向右移动一位则可以获得真实的结果值
        奇数末尾必定为1，向右移动一位获取到真实的1的结果值 + 1
        可以得到结果如下
        F[i] = F[i / 2] + F[i % 2]
        '''
        dp = [0] * (num + 1)
        for i in range(1, num + 1):
            dp[i] = dp[i >> 1] + (i & 1)
            
        return dp

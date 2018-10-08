class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        没有思路参考大神的DP:
        
        学数据结构的时候，曾学过不同构的二叉树的种数为卡特兰数，其通项公式如下： 
        从求解子问题的角度来看本题： 
        1. 选取一个结点为根，就把结点切成左右子树 
        2. 以这个结点为根的可行二叉树数量就是左右子树可行二叉树数量的乘积 
        3. 所以总的数量是将以所有结点为根的可行结果累加起来。也就是上述公式。
        url: https://blog.csdn.net/chilseasai/article/details/50042501

        '''
        dp = [1, 1] + (n - 1) * [0]
        for i in range(1, n + 1):
            dp[i] = sum(dp[j] * dp[i - j - 1] for j in range(i))
            
        return dp[n]

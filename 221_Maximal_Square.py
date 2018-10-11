class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        '''
        DP 动态规划
        观察规律即可获得
        1 首先复制一次矩阵, 对0行0列进行初始化,遍历过程实际上可以看成是一个最小矩阵(2X2)进行判断,获取最小矩阵的最小值加1,则可以看做依次对矩阵进行覆盖遍历，变成一个对原有矩阵的缩放更新，一个3X3的矩阵的遍历只需要移动这个2X2的矩阵四次即可获得。
        2 对矩阵结果结果规划合并,每一行合并出一个结果，最后是一个列矩阵，再次合并得到最终的矩阵长度，平方即可得到最终矩阵中出现的正方形矩阵的面积。
        
        优化空间:
        因为只需要返回结果,不需要保持矩阵与原来一致
        可以直接在矩阵上进行动规计算,强制转换为int类型覆盖原来的数据同时进行规划结果覆盖
        空间复杂度O(1),时间复杂度O(N) / ？？？ O(N + m)
        '''
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0 if matrix[i][j] == '0' else 1 for j in range(n)] for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                
                
        ans = max(max(i) for i in dp)
        return ans**2
                    
        

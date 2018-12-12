class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # 解法 1:将矩阵沿对角线进行转置,之后沿中间列对折互换数据
        # 解法 2:将矩阵沿反对角线进行转置,之后沿中间行对折互换数据
        # Solution 2:
        n = len(matrix)
        for i in range(n):
            for j in range(n - i):
                matrix[i][j], matrix[n-1-j][n-1-i] = matrix[n-1-j][n-1-i], matrix[i][j]
        
        for i in range(n//2):
            for j in range(n):
                matrix[i][j], matrix[n-1-i][j] = matrix[n-1-i][j], matrix[i][j]

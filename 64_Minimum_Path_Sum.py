class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        '''
        
        动态规划
        1 首先计算除[0][0]位置以外的第0行和第0列的规划路线
        2 动态判断非0行和非0列搜索时选择最小路径进行更新数组，直到所有位置遍历完成，得到最后的规划路线最小值
        '''
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j > 0:
                    grid[i][j] += grid[i][j - 1]
                elif j == 0 and i > 0:
                    grid[i][j] += grid[i-1][j]
                elif i > 0 and j > 0:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[len(grid) - 1][len(grid[0]) - 1]

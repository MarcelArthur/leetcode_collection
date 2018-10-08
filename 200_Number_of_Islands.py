class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        '''
        DFS深度搜索遍历的同时更新周边的数字为'0',直到发现新的'1'为孤立的岛位置。
        url: https://leetcode.com/problems/number-of-islands/discuss/56349/7-lines-Python-~14-lines-Java
        LeetCode天才太真实了
        '''
        def island(i, j):
            if  0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                grid[i][j] = '0'
                list(map(island, (i + 1, i - 1, i, i), (j, j, j + 1, j - 1 )))
                return 1
            return 0
        return sum(island(i, j) for i in range(len(grid)) for j in range(len(grid[i])))
        

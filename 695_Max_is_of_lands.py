# !python3
# 使用递归分别计算各个区域的数据, 递归得到最大的岛的数据从而进行展示


def maxisoflands(grid):
    def dfs(grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
            return 0
        if grid[i][j]:
            grid[i][j] = 0
            return 1 + dfs(grid, i - 1, j) + dfs(grid, i + 1, j) + dfs(grid, i, j + 1) + dfs(grid, i, j - 1)
        return 0

    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                res = max(res, dfs(grid, i, j))
    return res
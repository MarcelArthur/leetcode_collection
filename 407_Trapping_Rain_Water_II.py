import heapq
class Solution:
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap:
            return 0
        # 动态规划DP
        # 状态转移方程 使用同样大小的矩阵进行计算
        # 优先队列 将周边的依次入组，之后依次弹栈更新周边状态
        m = len(heightMap)
        n = len(heightMap[0])
        hres = [[0] * n for _ in range(m)]
        visited = [[0] * n for _ in range(m)]
        heap = []
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m - 1 or j == n- 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = 1
        result = 0
        # 最小堆
        while heap:
            height, i, j = heapq.heappop(heap)
            for x, y in zip((1, 0, -1, 0), (0, 1, 0, -1)):
                nx, ny = i + x, j + y
                
                if nx < 0 or nx >= m or ny < 0 or ny >= n or visited[nx][ny]:
                    continue
                result += max(0, height - heightMap[nx][ny])
                heapq.heappush(heap, (max(height, heightMap[nx][ny]), nx, ny)) # 加入最大值，更新周边的位置入组，并且继续探测直至所有位置都完成探测即可。此处更新状态(状态转移方程)
                visited[nx][ny] = 1
        return result

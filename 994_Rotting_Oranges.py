class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque() 
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
        minutes = 0   
        while(q):
            found = False
            for _ in range(len(q)):
                i, j = q.popleft()
                for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_i = i + dir[0]
                    new_j = j + dir[1]

                    if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] == 1:
                        found = True
                        grid[new_i][new_j] = 2
                        q.append((new_i, new_j))
            if found:
                minutes += 1
        # Check whether any fresh oranges exist. Reason for this check is,
        # there are chances to have a fresh orange, since rotting happens only
        # in 4-direction.
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return minutes

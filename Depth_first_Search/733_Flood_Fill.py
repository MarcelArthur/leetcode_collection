#!python3
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # DFS 
        if not image:
            return image
        old, n, m = image[sr][sc], len(image), len(image[0])
        def dfs(i, j):
            image[i][j] = newColor
            for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= x < n and 0 <= y < m and image[x][y] == old:
                    dfs(x, y)
        if old != newColor:
            dfs(sr, sc)
        return image
    
    
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # BFS
        if not image:
            return image
        old, n, m = image[sr][sc], len(image), len(image[0])
        q = collections.deque([(sr, sc)])
        if old != newColor:
            while q:
                i, j = q.popleft()
                image[i][j] = newColor
                for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                    if 0 <= x < n and 0 <= y < m and image[x][y] == old:
                        q.append((x, y))
        return image
        

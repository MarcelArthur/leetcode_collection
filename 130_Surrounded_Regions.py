import collections
class Solution:
    # BFS
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dq = collections.deque([])
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i in [0, len(board) - 1] or j in [0, len(board[0]) - 1]) and board[i][j] == "O":
                    dq.append((i, j))
    
        while dq:
            r, c = dq.popleft()
            if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == "O":
                board[r][c] = "#"
                dq.append((r - 1, c)); dq.append((r + 1, c))
                dq.append((r, c + 1)); dq.append((r, c - 1))
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "#":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
                    
    # DFS
    def solve(self, board: List[List[str]]) -> None:
        """
        
        """
        def dfs(i, j, signs, d):
            signs.add((i, j))
            for di in d:
                x = di[0] + i
                y = di[1] + j
                if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == "O" and (x, y) not in signs:
                    dfs(x, y, signs, d)
        
        signs = set()
        d = [[0, -1], [-1, 0], [0, 1], [1, 0]]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i in [0, len(board) - 1] or j in [0, len(board[0]) - 1]:
                    if board[i][j] == "O" and (i, j) not in signs:
                        dfs(i, j, signs, d)
                        
        for i in range(1, len(board) - 1):
            for j in range(1, len(board[0]) - 1):
                if board[i][j] == "O" and (i, j) not in signs:
                    board[i][j] = "X"

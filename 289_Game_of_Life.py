class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # Solution 0: 
#         m = len(board)
#         n = len(board[0]) if m else 0
#         for i in range(m):
#             for j in range(n):
#                 count = 0 
#                 for a in range(max(i - 1, 0), min(i + 2, m)):
#                     for b in range(max(j - 1, 0), min(j + 2, n)):
#                         count += board[a][b] & 1
                
#                 if (count == 4 and board[i][j]) or count == 3:
#                     board[i][j] |= 2
                
#         for i in range(m):
#             for j in range(n):
#                 board[i][j] >>= 1
                
        
        # Solution 1: bit Manipulate
        
        dx = (1, 1, 1, 0, 0, -1, -1, -1)
        dy = (1, 0, -1, 1, -1, 1, 0, -1)
        for x in range(len(board)):
            for y in range(len(board[0])):
                lives = 0
                for z in range(8):
                    nx, ny = x + dx[z], y + dy[z]
                    lives += self.getCellStatus(board, nx, ny)
                if lives + board[x][y] == 3 or lives == 3:
                    board[x][y] |= 2
        for x in range(len(board)):
            for y in range(len(board[0])):
                board[x][y] >>= 1
    def getCellStatus(self, board, x, y):
        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
            return 0
        return board[x][y] & 1

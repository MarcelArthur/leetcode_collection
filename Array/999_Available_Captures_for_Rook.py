#!python3
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for i in range(8):
            for j in range(8):
                if board[i][j] == "R":
                    _x, _y = i, j
        res = 0 
        for i, j in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            x, y = _x + i, _y + j
            while 0 <= x < 8 and 0 <= y < 8:
                if board[x][y] == "p": 
                    res += 1
                if board[x][y] != ".":
                    break
                x, y = x + i, y + j
        return res

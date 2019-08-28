#!python3
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        M = len(matrix)
        N = len(matrix[0])
        res = []
        for i in range(M):
            for j in range(N):
                if i == 0 or j == 0 and (i, j) not in res:
                    res.append((i, j))
        
        for x, y in res:
            x, y, _x, _y = x + 1, y + 1, x, y
            while 0 <= x < M and 0 <= y < N:
                if matrix[x][y] != matrix[_x][_y]:
                    return False
                x, y, _x, _y = x + 1, y + 1, x, y
        return True

# one liner
# https://leetcode.com/problems/toeplitz-matrix/discuss/113385/Python-Easy-and-Concise-Solution
# 大佬解法
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        return all(r1[:-1] == r2[1:] for r1, r2 in zip(matrix, matrix[1:]))

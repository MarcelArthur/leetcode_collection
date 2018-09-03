class Solution:
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        row_length = len(board)
        cow_length = len(board[0])
        res = 0
        for i in range(row_length):
            for j in range(cow_length):
                if board[i][j] == '.' or (i > 0 and board[i-1][j] == 'X') or (j > 0 and board[i][j - 1] == 'X'):
                    continue
                res += 1
        return res
        

class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        '''
        低效深度搜索
        Solution 1:
        深度的遍历所有路径,如果能够有匹配到的结果则返回结果为True,否则则返回False, 递归直到所有结果归并
        '''
        self.col = len(board)
        self.row = len(board[0])
        if not word:
            return False
        
        for i in range(self.col):
            for j in range(self.row):
                if self.DFS(board, i, j, word):
                    return True
        return False
    
    def DFS(self, board, i, j, word):
        if len(word) == 0:
            return True
        if i < 0 or i >= self.col or j < 0 or j >= self.row or word[0] != board[i][j]:
            return False
        tmp = board[i][j]
        board[i][j] = '#'  # avoid visit again
        res = self.DFS(board, i - 1, j, word[1:]) or self.DFS(board, i + 1, j, word[1:]) or self.DFS(board, i, j - 1, word[1:]) or self.DFS(board, i, j + 1, word[1:])
        board[i][j] = tmp
        return res
        

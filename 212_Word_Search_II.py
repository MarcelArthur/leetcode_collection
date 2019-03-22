class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0]:
            return
        R = len(board)
        C = len(board[0])
        root = dict()
        for word in words:
            trie = root
            for c in word:
                if c not in trie:
                    trie[c] = {}
                trie = trie[c]
            trie["#"] = word
        
        def dfs(i, j, trie):
            if "#" in trie:
                ans.add(trie["#"])
            c, board[i][j] = board[i][j], ""
            if i and board[i-1][j] in trie:
                dfs(i-1, j, trie[board[i-1][j]])
            if i < R - 1 and board[i+1][j] in trie:
                dfs(i+1, j, trie[board[i+1][j]])
            if j and board[i][j-1] in trie:
                dfs(i, j-1, trie[board[i][j-1]])
            if j < C - 1 and board[i][j+1] in trie:
                dfs(i, j+1, trie[board[i][j+1]])
            board[i][j] = c
            
        ans = set()
        for i in range(R):
            for j in range(C):
                if board[i][j] in root:
                    dfs(i, j, root[board[i][j]])
        return list(ans)

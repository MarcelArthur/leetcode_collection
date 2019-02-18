class Solution:
    def orderlyQueue(self, S:'str', K:'int') -> 'str': 
        # 终于有入参合法性校验了, 解题思路如下
        # https://marcelarthur.xyz/Leetcode_899_Orderly_Queue/
        if K == 1:
            return min(S[i:] + S[:i] for i in range(len(S)))
        return ''.join(sorted(S)


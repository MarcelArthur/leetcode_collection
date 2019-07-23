#!python3
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        # Directed Graph  
        # 类似lettcode 227, 统计信任和被信任的次数，从而确认法官的位置
        res_map = [0] * (N+1)
        for a, b in trust:
            res_map[a] -= 1
            res_map[b] += 1
            
        for i in range(1, N+1):
            if res_map[i] == N - 1:
                return i
        return -1

#!python3
class Solution:
    # 转置矩阵
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        return list(zip(*A))

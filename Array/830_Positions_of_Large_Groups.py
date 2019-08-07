#!python3
class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        if len(S) < 3:
            return []
        # two points
        res = []
        i = 0
        for j in range(len(S)):
            if j == len(S) - 1 or S[j] != S[j+1]:
                if j - i + 1 >= 3:
                    res.append([i, j])
                i = j + 1
        return res

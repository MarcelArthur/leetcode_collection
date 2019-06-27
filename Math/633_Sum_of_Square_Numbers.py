#!python3
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        res = set()
        idx = 0
        while idx * idx <= c:
            res.add(idx*idx)
            idx += 1
        
        for v in res:
            if (c-v) in res:
                return True
        return False

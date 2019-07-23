#!python3
class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        if not A:
            return [False]
        res = []
        res_str = ""
        for v in A:
            res_str += str(v)
            if int(res_str, 2) % 5 == 0:
                res.append(True)
            else:
                res.append(False)
        return res
        
        
class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        for i in range(1, len(A)):
            A[i] += A[i-1] * 2 % 5
        return [x % 5 == 0 for x in A]

class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        c, res = 0, []
        for i in A:
            c = (c * 2 + i) % 5
            res.append(c == 0)
        return res


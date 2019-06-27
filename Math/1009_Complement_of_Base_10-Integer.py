#!python3
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        n = bin(N)[2:]
        r = list()
        for i in n:
            if i == "1":
                r.append("0")
            else:
                r.append("1")
        return int("".join(r), 2)    

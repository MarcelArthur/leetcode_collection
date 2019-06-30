#!python3
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        # Solution 1
        A = int("".join([str(x) for x in A]))
        C = A + K
        return [int(x) for x in list(str(C))]
        # Solution  2
        return [int(x) for x in list(str(int("".join(str(x) for x in A)) + K))]
        # Solution 3
        c = 0
        for i in A:
            c = c*10 + i
        K = K+c
        L = []
        s = str(K)
        for i in s:
            L.append(int(i))
        return L

#!python3
# Solution KMP 算法 O(N+M) M为小n的次数


class Solution:

    def repeatedStringMatch(self, A: str, B: str) -> int:
        def match(S, P):
            pi = [0] * len(P)
            k = 0
            for i in range(1, len(P)):
                while k and P[k] != P[i]:
                    k = pi[k-1]
                if P[i] == P[k]:
                    k += 1
                pi[i] = k
            k = 0
            for i, c in enumerate(S):
                while k and P[k] != c:
                    k = pi[k-1]
                if P[k] == c:
                    k += 1
                if k == len(P):
                    return True
            return False
        n = -(-len(B)//len(A))
        for i in range(n, n+2):
            if match(A*i, B):
                return i
        return -1

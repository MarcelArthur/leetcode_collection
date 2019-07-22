#!python3
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        
        differents = 0
        differentIndex = [-1, -1]
        differentIndexcur = 0
        
        for i in range(len(A)):
            if A[i] != B[i]:
                differentIndex[differentIndexcur % 2] = i
                differents += 1
                differentIndexcur += 1
        
        if differents > 2 or differents == 1:
            return False
        elif differents == 2:
            return A[differentIndex[0]] == B[differentIndex[1]] and A[differentIndex[1]] == B[differentIndex[0]]
        else:
            return len(set(A)) != len(A)

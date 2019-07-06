#!python3
from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        # solution 1
        # Time O(N+lgN) Space O(1)
        for i in range(len(A)):
            A[i] = A[i] * A[i]
        A.sort()
        return A

    def sortedSquares(self, A: List[int]) -> List[int]:
        # solution 2
        # Space O(N) Time O(N+lgN)
        return sorted(list(map(lambda y: y * y, A)))

    def sortedSquares(self, A: List[int]) -> List[int]:
        # solution 3
        return sorted([i ** 2 for i in A])

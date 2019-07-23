#!python3
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        # 没啥说的，按照题目，逐行反转再取反
        return [[0 if x else 1 for x in line[::-1]]for line in A]

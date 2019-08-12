#!python3
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        # 3n == sum(A)
        s = sum(A)
        if s % 3 != 0:
            return False
        s /= 3
        acc = 0
        targets = [s * 2, s]
        for a in A:
            acc += a
            if acc == targets[-1]:
                targets.pop()
            if not targets:
                return True
        return False

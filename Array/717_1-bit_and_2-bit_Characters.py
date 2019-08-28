#!python3
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        n = len(bits) - 1
        while i < n:
            i += 1 + bits[i]
        return i == n

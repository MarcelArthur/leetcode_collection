#!python3
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        for v in s.split(" ")[::-1]:
            if v:
                return len(v)
        return 0

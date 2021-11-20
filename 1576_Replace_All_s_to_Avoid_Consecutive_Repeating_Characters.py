class Solution:
    def modifyString(self, s: str) -> str:
        if not s:
            return s
        s = list(s)
        for i in range(len(s)):
            if s[i] == "?":
                for c in "abc":
                    if (i == 0 or s[i-1] != c) and (i == len(s) - 1 or s[i+1] != c):
                        s[i] = c
                        break
        return "".join(s)

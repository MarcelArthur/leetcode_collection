class Solution:
    def isPalindrome(self, s: str) -> bool:
        for i in range(len(s)):
            if s[i] != s[len(s)-1-i]: return False
        return True
    
    def dfs(self, s, stringlist):
        if len(s) == 0: self.res.append(stringlist)
        for i in range(1, len(s)+1):
            if self.isPalindrome(s[:i]):
                self.dfs(s[i:], stringlist + [s[:i]])
    
    
    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        self.dfs(s, [])
        return self.res

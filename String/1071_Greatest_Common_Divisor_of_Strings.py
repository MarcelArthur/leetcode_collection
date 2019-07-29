#!python3
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # 辗转相除法
        if len(str1) < len(str2):
            str1, str2 = str2, str1
            
        while str2:
            
            a = len(str1) % len(str2)
            n = len(str1) // len(str2)
            
            if a== 0 and str1 != str2 * n or a > 0 and str1[:-a] != str2 * n:
                return ""
            
            if a == 0:
                return str2
            
            str1, str2 = str2, str1[-a:]
        return str2

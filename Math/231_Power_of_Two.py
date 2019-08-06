#!python3
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        s = bin(n)[2:]
        if s.count("1") > 1:
            return False
        return True
    
    
    
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        if n % 2:
            return False
        return self.isPowerOfTwo(n//2)


#!python3
class Solution:
    def fib(self, N: int) -> int:
        if N < 2:
            return N
        a, b = 0, 1
        for i in range(1, N):
            a, b = b, a + b
        return b 
        

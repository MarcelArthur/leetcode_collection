# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.q = []
        
        
    def read(self, buf: List[str], n: int) -> int:
        buf_idx = 0
        while len(self.q) > 0 and buf_idx < n:
            buf[buf_idx] = self.q.pop(0)
            buf_idx += 1
        
        buf4 = [""] * 4
        
        while buf_idx < n:
            count = read4(buf4)
            if count == 0: 
                break
            self.q += buf4[:count]
            count = min(count, n - buf_idx)
            for i in range(count):
                buf[buf_idx] = self.q.pop(0)
                buf_idx += 1
        
        return buf_idx 

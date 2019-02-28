class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        self.map = {}
        
        for i in blacklist:
            self.map[i] = 1
            
        self.M = N - len(blacklist)
        for i in blacklist:
            if i < self.M:
                N -= 1
                while N in self.map:
                    N -= 1
                self.map[i] = N
                
    def pick(self) -> int:
        res = random.randint(0, self.M - 1)
        return self.map[res] if res in self.map else res


# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()



#!python3
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        return sorted([[r, c] for r in range(R) for c in range(C)], key=lambda x: abs(x[0]-r0)+abs(x[1]-c0))

# 计算曼哈顿距离
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        dist, ans = [], []
        for r in range(R):
            for c in range(C):
                dist += [abs(r-r0) + abs(c-c0)]
                ans += [[r,c]]
        dist, ans = zip(*sorted(zip(dist, ans)))
        return ans
    

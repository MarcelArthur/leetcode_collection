#!python3
class Solution:
    # two points
    def maxDistToClosest(self, seats: List[int]) -> int:
        res, last, n = 0, -1, len(seats)
        for i in range(n):
            if seats[i]:
                res = max(res, i if last < 0 else (i - last) // 2)
                last = i 
        return max(res, n - 1 - last)
# 遍历两次, 两边各遍历一次，找到符合要求的最大值
# @负明雪烛
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        index = - 20000
        size = len(seats)
        ans = [0] * size
        for i in range(size):
            if seats[i]:
                index = i
            else:
                ans[i] = abs(i - index)
        index = - 20000
        for j in range(size - 1, -1, -1):
            if seats[j]:
                index = j
            else:
                ans[j] = min(abs(j - index), ans[j])
        return max(ans)

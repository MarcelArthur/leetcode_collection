#!python3
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        # https://leetcode.com/problems/largest-triangle-area/discuss/122711/C%2B%2BJavaPython-Solution-with-Explanation-and-Prove
        # 
        return max(0.5 * abs(i[0] * j[1] + j[0] * k[1] + k[0] * i[1]- j[0] * i[1] - k[0] * j[1] - i[0] * k[1])
            for i, j, k in itertools.combinations(points, 3))

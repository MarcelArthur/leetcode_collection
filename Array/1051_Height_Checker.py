#!python3
class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        new_heights = sorted(heights)
        res = 0
        for v1, v2 in zip(heights, new_heights):
            if v1 != v2:
                res += 1
        return res

class Solution(object):
    def heightChecker(self, heights):
        A = sorted(heights)
        res = [i for i in map(lambda x, y: x - y, heights, A) if i != 0]
        return len(res)

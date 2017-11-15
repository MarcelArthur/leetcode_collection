import itertools
class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # 感谢高效的itertool的package内容
        cb = [list(x) for x in itertools.combinations([y for y in range(1, n+1)], k)]
        return cb
            

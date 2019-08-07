#!python3
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # Time O(N) Space O(100)
        m = {x:0 for x in range(100)}
        res = 0
        for dom in dominoes:
            k1 = dom[0] * 10 + dom[1]
            k2 = dom[1] * 10 + dom[0]
            res += m[k1]
            if k1 != k2:
                res += m[k2]
            m[k1] += 1
        return res
    
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # Time O(NlogN + N) Space O(N)
        _len = len(dominoes)
        dominoes = map(tuple, map(sorted, dominoes))
        d = collections.Counter(dominoes)
        res = 0
        for k, v in d.items():
            if v >= 2:
                res += v * (v - 1) // 2
        return res

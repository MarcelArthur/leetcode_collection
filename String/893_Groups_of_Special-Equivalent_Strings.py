#!python3
class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        v = collections.defaultdict(int)
        for s in A:
            even = ''.join(sorted(s[::2]))
            odd = ''.join(sorted(s[1::2]))
            v[(even, odd)] += 1    
        return len(v)
    
class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        return len(set("".join(sorted(w[:;2])) + "".join(sorted(w[1::2])) for w in A))

#!python3
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        N = collections.Counter(nums)
        return max([N[x] + N[x+1] for x in N if x+1 in N] or [0])

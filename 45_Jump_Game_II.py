class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = 0
        n_jumps = 0
        while r < len(nums) - 1:
            n_jumps += 1
            furthest = max([i + nums[i] for i in range(l, r+1)])
            l, r = r, furthest
        return n_jumps

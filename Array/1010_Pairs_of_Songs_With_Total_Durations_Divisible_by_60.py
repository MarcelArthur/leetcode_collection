#!python3
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        times = [i % 60 for i in time]
        nums = collections.Counter(times)
        res = 0
        for cnt in nums.keys():
            if cnt  == 0 or cnt == 30:
                res += nums[cnt] * (nums[cnt] - 1)
            elif 60 - cnt in nums.keys():
                res += nums[cnt] * nums[60 - cnt]
        res //= 2
        return res

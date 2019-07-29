#!python3
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums.index(max(nums))
        nums_sort = sorted(nums)
        return nums.index(max(nums)) if nums_sort[-1] >= nums_sort[-2]*2 else -1

    
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        # Time O(N) Space O(1)
        if len(nums) == 0:
            return -1
        
        highest = -1
        secondehighest = -1
        highindex = 0
        for i, v in enumerate(nums):
            if v >= highest:
                secondhighest = highest
                highest = v
                highindex = i
            elif v > secondhighest:
                secondhighest = v
        
        if highest < secondhighest * 2:
            highindex = -1
        return highindex
                

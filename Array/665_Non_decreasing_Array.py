#!python3
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        cnt = 1
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                if cnt == 0:
                    return False
                if i == 1 or nums[i] >= nums[i-2]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]
                cnt -= 1
        return True

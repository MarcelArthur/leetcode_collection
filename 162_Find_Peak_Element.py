class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Solution 0: My Clean Solution
        if not nums:
            return 0
        nums = [float('-inf')] + nums + [float('-inf')]
        result = 0
        for i in range(1, len(nums)-1):
            if nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
                return i - 1
        return nums.index(max(nums))
        
        # Solution 1:时间复杂度O(N),但好像不太严谨
        # for i in range(1, len(nums) - 1):
        #     if nums[i - 1] < nums[i] > nums[i + 1]:
        #         return i
        # return nums.index(max(nums))
        

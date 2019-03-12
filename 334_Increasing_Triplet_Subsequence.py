class Solution:
    """
    Solution 1:
    题意: 查找连续递增子序列长度为3
    (1) 用first和second分别表示当前最小的数和第二小的数，当遍历到连续且大于第二小的数时，返回True。
    (2) 时间复杂度为O(N), 空间复杂度为常数。
    """
    def increasingTriplet(self, nums: 'List[int]') -> 'bool':
        
#         if len(nums) < 3:
#             return False
#         first = float('inf')
#         second = float('inf')
#         for i in range(len(nums)):
#             if nums[i] < first:
#                 first = nums[i]
#             elif first < nums[i] < second:
#                 second = nums[i]
#             if nums[i] > second:
#                 return True
#         return False
    # Solution 2: 思路与1相同，更加简洁，second不一定在first之后，如果，达成连续递增子序列即可。
        first = second = float("inf")
        
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
        
    

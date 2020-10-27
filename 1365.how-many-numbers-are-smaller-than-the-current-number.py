#
# @lc app=leetcode id=1365 lang=python3
#
# [1365] How Many Numbers Are Smaller Than the Current Number
#

# @lc code=start
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        #  bucketsort
        # buckets = [0] * 101

        # for n in nums:
        #     buckets[n] += 1

        # pervious = 0
        # for i, v in enumerate(buckets):
        #     if v != 0:
        #         buckets[i] = pervious
        #         pervious += v
            
        # return [buckets[num] for num in nums]

        # bisect
        import bisect
        sorted_nums = sorted(nums)
        return [bisect.bisect_left(sorted_nums, num) for num in nums]

# @lc code=end


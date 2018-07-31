# 社区高效答案， 二分查找速度应该是最佳的，其实主要是乱序情况下的二分查找, 可是还是感觉不太快啊= = （而且这Leetcode也太不靠谱了，这样偶尔居然还能runtime Error）
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        lo = 0
        ri = len(nums) - 1
        while lo <= ri:
            mid = (lo + ri) // 2
            left_re, right_re, mid_re = nums[lo], nums[ri], nums[mid] 
            if target in (left_re, right_re, mid_re):
                return True
            if left_re < right_re:
                if mid_re < target:
                    lo = mid + 1
                else:
                    ri = mid - 1
            elif left_re > right_re:
                if mid_re >= left_re:
                    if left_re < target < mid_re:
                        ri = mid - 1
                    else:
                        lo = mid + 1
                else:
                    if mid_re < target < right_re:
                        lo = mid + 1
                    else:
                        ri = mid - 1
            else:
                lo += 1
                ri -= 1
        return False
                
                     
        # if not nums:
        #     return False
        # if target in set(nums):
        #     return True
        # return False
        

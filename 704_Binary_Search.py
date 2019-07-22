#!python3
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        back = len(nums) - 1
        while start <= back:
            mid = (start + back) // 2
            if nums[mid] == target:
                return mid
            else:
                if nums[mid] < target:
                    start = mid + 1
                else:
                    back = mid -1
        return -1 
                

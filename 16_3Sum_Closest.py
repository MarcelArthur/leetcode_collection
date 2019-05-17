# -*- coding:utf-8 -*-


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        mindiff = max(nums)
        result = []
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums) - 1
            while(left < right):
                sum = nums[left] + nums[i] + nums[right]
                diff = abs(sum - target)

                if diff == 0:
                    return sum
                if diff < mindiff:
                    mindiff = diff
                    result = sum

                if sum > target:
                    left += 1
                elif sum < target:
                    right -= 1

        return result


if __name__ =='__main__':
    L = [-1, 2, 1, -4]
    S = Solution()
    r = S.threeSumClosest(L, 1)
    print(r)
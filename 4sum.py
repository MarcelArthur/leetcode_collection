# -*- coding:utf-8 -*-

# 通用解法
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        isodd = set()
        L = list()
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]: continue
            for j in range(i+1, len(nums)-2):
                if j > i + 1 and nums[j] == nums[j-1]:continue
                left = j + 1
                right = len(nums) - 1
                sum = target - nums[i] - nums[j]
                while left < right:
                    tmp = nums[left] + nums[right]
                    if sum == tmp:
                        QT = [nums[i], nums[j], nums[left], nums[right]]
                        L.append(QT)
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif sum > tmp:
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                    else:
                        right -= 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1


        return L


#??? 最快算法 83ms
    class Solutions(object):
        def fourSum(self, nums, target):
            """
            :type nums: List[int]
            :type target: int
            :rtype: List[List[int]]
            """
            nums.sort()
            ret = []
            n = len(nums)
            i = 0
            while i < n - 3:
                if i > 0 and nums[i] == nums[i - 1]:
                    i += 1
                    continue
                if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                    break
                if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
                    i += 1
                    continue
                l = i + 1
                while l < n - 2:
                    if l > i + 1 and nums[l] == nums[l - 1]:
                        l += 1
                        continue
                    if nums[i] + nums[l] + nums[l + 1] + nums[l + 2] > target:
                        break
                    if nums[i] + nums[l] + nums[n - 2] + nums[n - 1] < target:
                        l += 1
                        continue
                    dif = target - nums[i] - nums[l]
                    j = l + 1
                    k = n - 1
                    while j < k:
                        s = nums[j] + nums[k]
                        if s == dif:
                            ret.append([nums[i], nums[l], nums[j], nums[k]])
                            j += 1
                            k -= 1
                            while j < k and nums[j] == nums[j - 1]:
                                j += 1
                            while j < k and nums[k] == nums[k + 1]:
                                k -= 1
                        elif s > dif:
                            k -= 1
                        else:
                            j += 1

                    l += 1

                i += 1
            return ret
if __name__ == "__main__":
    C = [1, 0, -1, 0, -2, 2]
    S = Solution()
    print(S.fourSum(C, 0))

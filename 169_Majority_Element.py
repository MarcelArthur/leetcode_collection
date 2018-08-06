# !python3
# 经典算法问题 处理在一个n位数组中出现大于(n/2)次数的主元素


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maj = nums[0]
        count = 1
        for i in range(len(nums)):
            if count == 0:
                maj = nums[i]
                count += 1
            elif maj == nums[i]:
                count += 1
            else:
                count -= 1
        return maj


if __name__ == '__main__':
    mav = Solution()
    print(mav.majorityElement([1,2,2,2,2,2,2,3,4,5,2,2,2,6]))

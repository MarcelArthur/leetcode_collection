class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # Solution 1:重排序,首先从尾端向前查找两个相邻的升序元素,升序元素的前一个标记为partition,再从尾端查找一个大于partition的元素,与partition指向的元素进行互换,并且将partition之后位置的元素逆序排列再输出,得到重排序之后的结果。
        if len(nums) <= 1:
            return 
        partition = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                partition = i
                break
        if partition == -1:
            nums.reverse()
            return 
        else:
            for i in range(len(nums) - 1, partition, -1):
                if nums[i] > nums[partition]:
                    nums[i], nums[partition] = nums[partition], nums[i]
                    break
        nums[partition+1:len(nums)] = nums[partition+1:len(nums)][::-1]
        return 
        
            
            

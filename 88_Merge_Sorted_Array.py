# 瞎写也能过= = 不过说起来这个其实是合理排序和快速过滤的问题
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        length = m + n
        difference = len(nums1) + len(nums2) - length
        while difference:
            difference -= 1
            nums1.pop()
        nums1.extend(nums2)
        nums1.sort()
        
# 正确思路 排序排序~~
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i, j = m-1, n-1
        for idx in range(m + n -1, -1, -1):
            if i < 0:
                nums1[:idx+1] = nums2[:j+1]
                break
            if j < 0:
                break
            if nums1[i] > nums2[j]:
                nums1[idx] = nums1[i]
                i -= 1
            else:
                nums1[idx] = nums2[j]
                j -= 1
        
            

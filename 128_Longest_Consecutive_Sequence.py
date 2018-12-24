class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Solution 1: 由于排序在大量列表中进行处理耗时和内存使用较多，放弃使用排序。使用哈希表处理，遍历列表中的数字，如果数字在哈希表中，那么判断其前后两个数字是否在哈希表中，如果在，返回其哈希表中的映射值,否则返回0，然后我们记录对应的left + right + 1的值，并更新res的值，然后将d-left的值和d-right的值。
        res = 0 
        s = dict()
        for one in nums:
            if s.get(one):
                continue
            left = s.get(one - 1, 0)
            right = s.get(one + 1, 0)
            sums = left + right + 1
            s[one] = sums
            res = max(res, sums)
            s[one - left] = sums
            s[one + right] = sums
        return res
        # Solution 2:使用set集合存入所有数字，判断每个数字是否在集合中出现，如果出现则移除数字并且判断，前后两个数字pre和nextone是否出现过，如果存在则移除pre，并且pre-1，nextone同样处理。记录nextone - left - 1获得当前数字的连续序列。但是果然数据结构List查找时间太长= = TLE
                
                
        

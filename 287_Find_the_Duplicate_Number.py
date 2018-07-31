# emmmm  比较简单的一道题 不过实现方式确实非常多，以在社区看到的实现方式为例：
# Bitmap  安全高效,但是python版本的Bitmap需要实现Bitmap类型和具体的set, 判重方法，更多的是利用C++原生的byte数组实现的(有时间补充一下Bitmap实现)
# 二分查找 递归查找方式，不过需要定位一旦查到重复的队列就需要立即返回，时间复杂度可以接受，空间控制在O（1）范围内
# Hashset 去重(如下)
# 基本上也没有什么了
class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 
        nums_set = set()
        for num_one in nums:
            if num_one in nums_set:
                return num_one
            nums_set.add(num_one)
            

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        '''
        如何快速判断值域范围呢
        两两之间的值域范围是否重合
        Solution 1:过程主要分为两步
        第一步是首先排序合适的值域区间起点，将相似起点的值域区间升序排列。
        第二步是合并值域空间，主要是要处理下重合值域空间里的最大区间的终点值而不是后一个元素空间的终点值。这里要特别注意一下~
        '''
        if not intervals or len(intervals) == 1:
            return intervals
        # intervals.sort()
        
        intervals = sorted(intervals, key = lambda x: x.start)
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i].start > result[-1].end:
                result.append(intervals[i])
            else:
                result[-1].end = max(intervals[i].end, result[-1].end)
        return result

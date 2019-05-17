import bisect
import heapq
# 关于二分查找模块bisect的使用方法和场景。链接: https://www.cnblogs.com/beiluowuzheng/p/8452671.html && http://www.cnblogs.com/skydesign/archive/2011/09/02/2163592.html
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.med = list()

    def addNum(self, num: 'int') -> 'None':
        """
        type: 'None'
        """
        bisect.insort(self.med, num)

    def findMedian(self) -> 'float':
        """
        type: 'float'
        """
        if len(self.med) == 0:
            return 0
        mid = len(self.med) // 2
        if len(self.med) % 2 == 0:
            mid = len(self.med) // 2
            result = (self.med[mid - 1] + self.med[mid]) / 2
            return result
        return float(self.med[mid])
    

class MedianFinder(object):
    def __init__(self):
        self.med, self.odd, self.heaps = 0, 0, [[], []]

    def addNum(self, num: 'int') -> None:
        small, big = self.heaps
        if self.odd:
            self.heappushpop(big, max(x, self.med))
            self.heappushpop(small, -min(x, self.med))
            self.med = (big[0] - small[0]) / 2.0
        else:
            if x > self.med:
                self.med = self.heappushpop(big, x)
            else:
                self.med = self.heappushpop(small, -x)
        self.odd ^= 1
    
    def findMedian(self) -> float:
        return self.med




# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

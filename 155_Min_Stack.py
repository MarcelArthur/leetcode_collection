'''
挺有意思的设计,只在每次push的时候比对最新的元素是否是最小值,更新最小值列表，在列表内增加普通元素和最小值信息。可以让getMin由O(N)变成O(1)时间复杂度。提升效率,减少比对时间~        
'''
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        
        
        self.List = []        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x
        return self.List.append((x, curMin))

    def pop(self):
        """
        :rtype: void
        """
        self.List.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.List) == 0:
            return None
        else:
            return self.List[len(self.List) - 1][0]
            
        

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.List) == 0:
            return None
        else:
            return self.List[len(self.List) - 1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

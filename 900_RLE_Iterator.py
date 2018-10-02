class RLEIterator:

    def __init__(self, A):
        """
        :type A: List[int]
        """
        # 初始化方案
        # 两两一对，(N, X)N为显示X的个数，该元组表示实际的列表元素构造，解析映射到真实的列表元素，但是解析成真实列表Test Case使用大量内存导致内存溢出。实际上不需要转换出列表直接根据原有的列表信息可以处理映射关系
        
        '''
        解决方案:
        url:https://leetcode.com/problems/rle-iterator/discuss/176553/Python-simple-pointer-to-next-element
        1. 不单独构建新的列表结构，只标记取数的位置，迭代读取返回结果
        url: https://leetcode.com/problems/rle-iterator/discuss/175683/Python-Binary-Search-Solution-beats-100
        2. 组成取值列表和索引列表映射，next迭代方法内部使用二分查找索引列表快速返回取值所在的索引项位置，根据索引值获取到结果并且返回
        '''
        self.List = A
        self.length = len(A)
        self.i = 0

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        while self.i < self.length and self.List[self.i] < n:
            n -= self.List[self.i]
            self.i += 2
        
        if self.i >= self.length:
            return -1
        self.List[self.i] -= n
        return self.List[self.i + 1]


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)

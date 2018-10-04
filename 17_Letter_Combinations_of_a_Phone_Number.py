class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        '''
        经典回溯法题目:逐层递归合并每一层元素累加获得结果列表
        Solution1: 递归回溯逐层查找合适的组合项 AC 90%。代码如下
        '''
        
        if not digits:
            return []
        
        curr = ''
        result_curr = []
        dig_dict = [' ', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        self.dig_dict = dig_dict
        def DFS(digits, dig_dict, curr, index):
            if index == len(digits):
                if curr:
                    result_curr.append(curr)
                    return
            for i in dig_dict[int(digits[index])]:
                next_curr = curr + i
                DFS(digits, dig_dict, next_curr, index + 1)
        DFS(digits, dig_dict, '', 0)
        return result_curr
        
        '''
        Solution2: 原理同上，不过可以换成更简洁的写法，但是性能下降了 44ms 38% AC
        '''
#         res = ['']
#         for i in digits:
#             res = self.quicklyFind(int(i), res)
#         return res
            
#     def quicklyFind(self, dindex, orderList):
#         # 列表推导式的生成效率确实不太高
#         return [done + i for i in self.dig_dict[dindex] for done in orderList]
                

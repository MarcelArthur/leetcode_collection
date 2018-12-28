class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # Solution 1:之后再补
        def count_content(num):
            result, count, pre_one = "", 0, num[0]
            for digist in num:
                if digist == pre_one:
                    count += 1
                else:
                    result += str(count) + pre_one
                    pre_one = digist
                    count = 1
            result += str(count) + pre_one
            return result
        pre_value = '1'
        for i in range(1, n):
            pre_value = count_content(pre_value)
        return pre_value
        
                         
                        
                    
                

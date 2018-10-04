class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        Solution 1: 利用堆栈的特性将需要记录的左括号的位置push进栈中，之后每次遇到右括号弹出栈内元素, 如果弹出后栈内元素不为空，则根据最新的累加结果值比对最近一次入栈左括号的位置，得到最新的有效值，直到所有位置的值遍历结束。时间复杂度O(N),空间复杂度O(N)。
        
        '''
    
        stack = []
        total = 0 
        for i in range(len(s)):
            if s[i] == ')' and stack and s[stack[-1]] == '(':
                stack.pop()
                if not stack:
                    total = i + 1
                else:
                    total = max(total, i - stack[-1])
            else:
                stack.append(i)
        
        return total
    
        '''
        Solution 2:DP 动规
        url: https://blog.csdn.net/wusecaiyun/article/details/46867469
        之后补充
        '''
        

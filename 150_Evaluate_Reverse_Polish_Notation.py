import operator

class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        # https://leetcode.com/problems/evaluate-reverse-polish-notation/discuss/215008/Python-solution-using-stack-and-custom-divide-function
        stack = []
        
        ops = {'+': operator.add, '-': operator.sub, 
               '*': operator.mul, '/': self.divide}
        
        for t in tokens:
            if t not in ops:
                stack.append(int(t))
            else:
                r = stack.pop()
                l = stack.pop()
                
                val = ops[t](l, r)
                stack.append(val)
        
        return stack[-1]
    
    def divide(self, l, r):
        if (l < 0 and r > 0) or (l > 0 and r < 0):
            return - (abs(l) // abs(r))
        else:
            return l // r

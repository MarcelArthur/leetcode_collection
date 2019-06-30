#!python3
class Solution:
    """
    分治思想，记录每一块完整的大括号的内容处理不同的数据
    """
    def removeOuterParentheses(self, S: str) -> str:
        # No stack
        counter = 0
        result = ""
        start_location = []
        for i in range(len(S)):
            if S[i] == "(":
                counter += 1
                start_location.append(i)
            elif S[i] == ")" and counter > 0:
                counter -= 1
                if counter == 0:
                    result += S[start_location[0] + 1:i]
                    start_location = []
        return result
    
    def removeOuterParentheses(self, S: str) -> str:
        # One Stack
        res = ""
        stack = []
        
        basket = ""
        for v in S:
            if v == "(":
                stack.append(v)
            else:
                stack.pop()
            basket += v
            
            
            if not stack:
                res += basket[1:-1]
                basket = ""
        return res

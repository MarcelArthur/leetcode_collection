class Solution:
    # ans = []
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        '''
        奇妙解题思路:
        写一个过滤方法，依次过滤不符合的组合方式知道查找到合适的过滤方式后返回结果，非常奇妙。(就是时间复杂度有点高= =
        '''
        # def isvalid(s):
        #     ctr = 0
        #     for c in s:
        #         if c == '(':
        #             ctr += 1
        #         elif c == ')':
        #             ctr -= 1
        #             if ctr < 0:
        #                 return False
        #     return ctr == 0
        # level = {s}
        # while True:
        #     valid = list(filter(isvalid, level))
        #     if valid:
        #         return valid
        #     level = {s[:i] + s[i+1:] for s in level for i in range(len(s)) if s[i] in ('(', ')')}
        
        '''
        解题思路
        首先想到是深度搜索，然后找出不符合规则")"右括号的那一部分子字符串，进行深度搜索，依次尝试剔除其中不符合规则的元素，知道找到符合规则的结果，另外实际上如果存在另一个结果只需要找到对字符串逆置之后的结果对"("左括号内的内容进行剔除即可。
        '''
        def helper(i, j, pattern, s):
            cnt = 0
            for x in range(j, len(s)):
                if s[x] == pattern[0]:
                    cnt += 1
                if s[x] == pattern[1]:
                    cnt -= 1
                if cnt < 0:
                    for y in range(i, x + 1):
                        if s[y] == pattern[1] and (y == i or s[y - 1] != pattern[1]):
                            helper(y, x, pattern, s[:y] + s[y + 1:])
                    return
            
            if pattern[0] == '(':
                helper(0, 0, [')', '('], s[::-1])
            else:
                res.append(s[::-1])
        
        res = []
        helper(0, 0, ['(', ')'], s)
        return res
        

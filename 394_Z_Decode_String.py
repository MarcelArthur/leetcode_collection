import re
class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        '''
        大神解法
        直接通过正则匹配
        Time to out
        233333
        '''
        # while '[' in s:
        #     s = re.sub(r'(\d+)\[([a-z]*)\]', lambda x: int(x.group(1)) * x.group(2), s)
        # return s
        '''
        
        '''
        stack = []; curNum = 0; curString = ''
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num*curString
            elif c.isdigit():  # ???这个是什么情况呢
                curNum = curNum*10 + int(c)
            else:
                curString += c
        return curString

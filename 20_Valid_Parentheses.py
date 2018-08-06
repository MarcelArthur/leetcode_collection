# !python3
'''
高效数据结构+高效判断(如果新增的符号时,栈内没有元素或者没有对应元素则判断为假)
'''
from collections import deque


class Solution:
    def isValid(self, s):
        '''
        :param s:str
        :return:bool
        '''
        match ={')':'(', '}':'{', ']':'['}
        stack = deque()
        for c in s:
            if c not in match:
                stack.append(c)
            else:
                if not stack or stack.pop() != match[c]:
                    return False
        return True if not stack else False


if __name__ == '__main__':
    s = Solution()
    print(s.isValid('{{{}}}'))

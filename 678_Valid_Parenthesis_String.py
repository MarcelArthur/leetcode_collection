# 方法其实很多,一种是真的用堆栈实现合理性同时弹栈，判断是否符合状态 (大概率超时， 判断状态较多)
# 第二种: 可以记录每个坐标的位置放到对应hashmap当中， 从中遍历出合理的位置，
# 第三种: 首先过滤出来对应的规则，构建左括号stack和星号stack，既通过遍历O(N)的所有"(" AND '*', 优先处理正常的 ["()", "*)"] 情况，再次判定 ["*("] 这种情况，过滤出最后的结果。

class Solution:
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = list()
        star = list()
        for i in range(len(s)):
            if s[i] == '*':
                star.append(i)
            elif s[i] == '(':
                left.append(i)
            else:
                if not left and not star:
                    return False
                elif left:
                    left.pop()
                else:
                    star.pop()
        while left and star:
            if left[-1] > star[-1]:
                return False
            left.pop()
            star.pop()
        return left == []
# 社区高效算法 讲道理没看懂= =
# class Solution:
#     def checkValidString(self, s):
#         a, b = 0, 0
#         for c in s:
#             if c == '(': a += 1; b += 1
#             elif c == ')': a -= 1; b -= 1
#             else: a -= 1; b += 1
#             if b < 0:
#                 return False
#             a = max(0, a)
#         return a <= 0 <= b

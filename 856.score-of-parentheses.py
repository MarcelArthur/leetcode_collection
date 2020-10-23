#
# @lc app=leetcode id=856 lang=python3
#
# [856] Score of Parentheses
#

# @lc code=start
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        # stack, cur = [], 0
        # for i in S:
        #     if i == '(':
        #         stack.append(cur)
        #         cur = 0
        #     else:
        #         cur += stack.pop() + max(cur, 1)
        # return cur

        # O(1) Space
        # We count the number of layers.
        res = l = 0
        for a, b in zip(S, S[1:]):
            if a + b == "()":
                res += 2 ** l
            l += 1 if a == "(" else -1
        return res



# @lc code=end


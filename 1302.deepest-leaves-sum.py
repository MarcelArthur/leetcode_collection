#
# @lc app=leetcode id=1302 lang=python3
#
# [1302] Deepest Leaves Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        res = 0
        stack = [root]
        while stack:
            curr = []
            d = 0
            for node in stack:
                d += node.val
                if node.left:
                    curr.append(node.left)
                if node.right:
                    curr.append(node.right)
            if d:
                res = d
            stack = curr
        return res

# @lc code=end


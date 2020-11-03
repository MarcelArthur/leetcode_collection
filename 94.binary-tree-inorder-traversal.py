#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        cur = root
        result = []
        stack = []
        # stack.append(root)
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            # else:
            cur = stack.pop()
            result.append(cur.val)
            cur = cur.right
        return result 
# @lc code=end


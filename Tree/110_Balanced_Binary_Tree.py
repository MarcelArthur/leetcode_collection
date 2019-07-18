#!python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 题承接 104
class Solution:
    """
    好难受，想到了没写出来orz.果然还是要多动手
    """
    def isBalanced(self, root: TreeNode) -> bool:
        self.balanced = True
        
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if abs(left - right) > 1:
                self.balanced = False
            return max(left, right) + 1
        dfs(root)
        return self.balanced

    
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if left == -1 or right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return max(left, right) + 1
        r = dfs(root)
        return r != -1

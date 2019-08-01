#!python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# DFS
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if root.val > q.val and root.val > p.val:
                root = root.left
            elif root.val < q.val and root.val < p.val:
                root = root.right
            else:
                return root

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val > q.val and root.val > p.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < q.val and root.val < p.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root

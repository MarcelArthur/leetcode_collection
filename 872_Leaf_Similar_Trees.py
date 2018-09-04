# 水题
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        root1_result = []
        root2_result = []
        def iter_leaf(root, root_result):
            if not root.left and not root.right:
                root_result.append(root.val)
                return 
            if root.left:
                iter_leaf(root.left, root_result) 
            if root.right:
                iter_leaf(root.right, root_result)
        iter_leaf(root1, root1_result)
        iter_leaf(root2, root2_result)

        return root1_result == root2_result

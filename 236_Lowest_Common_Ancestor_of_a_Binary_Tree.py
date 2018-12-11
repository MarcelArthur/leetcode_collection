# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Solution 1:中序遍历递归查找LCA，最低公共祖先,同时进行快速判断
        if not root or p == root or q == root:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        if left and left != p and left != q:
            return left
        right = self.lowestCommonAncestor(root.right, p, q)
        if right and right != p and right != q:
            return right
        if left and right:
            return root
        return left if left else right

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 修剪二叉搜索树


class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        # 如果为None则返回None,不继续搜索
        if not root:
            return root
        if root.val < L:
            return self.trimBST(root.right, L, R)
        if root.val > R:
            return self.trimBST(root.left, L, R)
        # 如果全部符合条件，则把符合条件的节点接这个节点之后
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        return root

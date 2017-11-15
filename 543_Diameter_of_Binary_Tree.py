# python3
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None




class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def Maxdeep(root):
            if not root:
                return 0
            left = Maxdeep(root.left)
            right = Maxdeep(root.right)
            self.res = max(self.res, left+ right)
            return max(left, right) + 1
        Maxdeep(root)
        return self.res


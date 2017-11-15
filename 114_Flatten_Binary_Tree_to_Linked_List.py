# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        # if root.val is None:
        #     return None
        # 分解问题
        # 1. 递归方法解决(推荐)
        # 2. 非递归方法解决
        # DFS方法遍历二叉树找到最左边的左子树，回归到父节点，将父节点的左子节点接在原右子节点上，左子节点置空，继续遍历右子节点至全空时，将原右子节点接到新右子节点的右子节点上，继续返回到父节点做同样的操作。(其实是大问题拆分为子问题的方式进行)
        if not root:
            return 
        if root.left:
            self.flatten(root.left)
        if root.right:
            self.flatten(root.right)
        right_node = root.right
        root.right = root.left
        root.left = None
        while root.right:
            root = root.right
        root.right = right_node
    

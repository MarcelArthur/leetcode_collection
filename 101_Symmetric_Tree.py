# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # stack = [root]
        '''
        url:https://leetcode.com/problems/symmetric-tree/discuss/33068/6line-AC-python
        感谢lee215的迭代实现 
        思路: 重点是每一次更新最新一层的栈内元素，同时比对逆置列表和列表，直到每一层内的左右子树值列表比对完成
        '''
        # queue = [root]
        # while queue:
        #     values = [i.val if i else None for i in queue]
        #     if values != values[::-1]: return False
        #     queue = [child for i in queue if i for child in (i.left, i.right)]
        # return True
        
        if not root:
            return True
        return self.DFS(root.left, root.right)
    
    def DFS(self, left, right):
        if not left and not right:
            return True
        
        if left and right and left.val == right.val and self.DFS(left.left, right.right) and self.DFS(left.right,right.left):
            return True
        return False
        
        

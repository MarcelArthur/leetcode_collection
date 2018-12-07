# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 合并两个二叉树
    # Solution 1:递归判断组合二叉树，实现二叉树逐结点合并。优点:没有使用额外的内存 缺点:递归归并组合二叉树耗时较长
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        
        if not t1 and not t2:
            return None
        if not t1 and t2:
            return t2
        if not t2 and t1:
            return t1
        if t1 and t2:
            t1.val += t2.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
        return t1
    
    # Solution 2: 利用额外的内存,但是耗时比较少(存疑,因为不能指向同一个内存地址(同一个TreeNode对象)，最后结果会出现一个None值无法和有效值进行归并,这看起来有点奇怪)  Golang实现无异常
#     def dfs(self, node, t):
#         if not t:
#             return 
#         if not node:
#             node = TreeNode(0)
        
#         node.val += t.val
#         node.left = self.dfs(node.left, t.left)
#         node.right = self.dfs(node.right, t.right)
#         return node
    
#     def mergeTrees(self, t1, t2):
#         if not t1 and not t2:
#             return None
        
#         m = TreeNode(0)
        
#         m = self.dfs(m, t1)
#         m = self.dfs(m, t2)
        
#         return m
        
        
        
        

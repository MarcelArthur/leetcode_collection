# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        '''
        可迭代版本
        更新记录每一层有效的值，并计入结果列表中 AC 99 %
        层次遍历二叉树
        '''
        self.cur_varlist = []
#         if not root:
#             return []
#         stack = [root]
#         res = []
#         while stack:
#             values = [i.val for i in stack if i]
#             res.append(values)
#             stack = [child for i in stack if i for child in (i.left, i.right) if i.left or i.right]
#         return res
        self.DFS(root, 0)
        return self.cur_varlist
    
        '''
        DFS
        '''
    def DFS(self, cur, depth):
        if not cur:
            return 
        if depth >= len(self.cur_varlist):
            self.cur_varlist.append([cur.val])
        else:
            self.cur_varlist[depth].append(cur.val)
            
        self.DFS(cur.left, depth + 1)
        self.DFS(cur.right, depth + 1)

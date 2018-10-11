# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        '''
        常规的深度遍历
        最优决策
        刚开始思路偏了 以为每次拒绝后一定会偷
        实际上这里需要做决策,每到一个节点选择最优方案,不停的决策获得最优结果
        通常情况是偷和拒绝两种情况所以这里只需要考虑每个节点深度遍历的同时进行决策即可
        '''
        return self.DFS(root)[1]
        
    def DFS(self, root):
            if root is None:
                return (0, 0)
            l = self.DFS(root.left)
            r = self.DFS(root.right)
            return (l[1] + r[1], max(l[1] + r[1], l[0] + r[0] + root.val))
        
        
        
        

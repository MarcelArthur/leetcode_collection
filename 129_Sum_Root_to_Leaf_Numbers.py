# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 思路: 其实是所有叶子节点的值 + 层级 * 10 * 每层节点的值进行累加获得结果，递归到叶子节点，再对遍历过程中的节点值记录并且转换就能得到结果
# Python比较容易进行累加和数据类型的转换
# 除了递归，那迭代呢？
# BFS如何判断广度的节点等级
class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        sumnumber_result = 0
        if not root:
            return sumnumber_result
        root_queue = [root]
        while root_queue:
            new_root = root_queue.pop(0)
            if not new_root.left and not new_root.right:
                sumnumber_result += new_root.val
            if new_root.left:
                new_root.left.val += new_root.val * 10
                root_queue.append(new_root.left)
            if new_root.right:
                new_root.right.val += new_root.val * 10
                root_queue.append(new_root.right)
        return sumnumber_result
    
# 递归没有难度就不写了
                
                

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    res = 0
    def pathSum(self, root, sum_num):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        # Solution 1:以每个节点作为根节点进行前序遍历,查找每一条路径上的值是否和预期值相等。 AC 28%
        if not root:
            return 0
        res = self.findPath(root, 0, sum_num) + self.pathSum(root.left, sum_num) + self.pathSum(root.right, sum_num)
        return res
        
    def findPath(self, node, cursum, sum_num):
        if not node:
            return 0
        cursum += node.val
        return (cursum == sum_num) + self.findPath(node.left, cursum, sum_num) + self.findPath(node.right, cursum, sum_num)
        # Solution 2: 另一种写法 当然并没有什么用 AC 23%
    
#         if not root:
#             return 0
#         self.pathSum(root.left, sum_num)
#         self.pathSum(root.right, sum_num)
#         self.helper(root, sum_num)
#         return self.res
        
#     def helper(self, node, sum_num):
#         if not node:
#             return 0
#         if sum_num - node.val == 0:
#             self.res += 1
#         self.helper(node.left, sum_num - node.val)
#         self.helper(node.right, sum_num - node.val)
        

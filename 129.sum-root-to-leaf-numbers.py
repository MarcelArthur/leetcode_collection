#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return  0
        def dfs(root, num_sum, res) -> None:
            if not root:
                return 
            num_sum = num_sum * 10 + root.val
            if not root.left and not root.right:
                res.append(num_sum)
            dfs(root.left, num_sum, res)
            dfs(root.right, num_sum, res)
        
        res = []
        dfs(root, 0, res)
        return sum(res)
            

# @lc code=end


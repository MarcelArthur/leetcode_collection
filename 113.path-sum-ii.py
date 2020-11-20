#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, Sum: int) -> List[List[int]]:
        result = []
        def dfs(root, res, target):
            if not root:
                return None
            if root.val == target and not root.left and not root.right:
                result.append(res + [root.val])
                return

            
            dfs(root.left, res + [root.val], target - root.val)
            dfs(root.right, res + [root.val], target - root.val)
        dfs(root, [], Sum)
        return result
            

# @lc code=end


#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return  []
        def dfs(root, path_str, paths) -> None:
            if not root:
                return 
            if path_str:
                path_str += "->"
            path_str += str(root.val)
            if not root.left and not root.right:
                paths.append(path_str)
            dfs(root.left, path_str, paths)
            dfs(root.right, path_str, paths)
        res = []
        dfs(root, "", res)

        return res


# @lc code=end


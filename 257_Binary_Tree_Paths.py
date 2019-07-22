#!python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 弱渣写法(我的思路)
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.res = []
        def dfs(root, path):
            if not root:
                return
            path += "->{}".format(root.val)
            dfs(root.left, path)
            dfs(root.right, path)
            if not root.left and not root.right:
                self.res.append(path[2:])
        dfs(root, "")
        return self.res

# 大佬写法
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        return [str(root.val) + "->" + path for kid in (root.left, root.right) if kid for path in self.binaryTreePaths(kid)] or [str(root.val)]
# 正常写法
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        return [str(root.val) + "->" + i for i in self.binaryTreePaths(root.left)] + [str(root.val) + "->" + i for i in self.binaryTreePaths(root.right)]

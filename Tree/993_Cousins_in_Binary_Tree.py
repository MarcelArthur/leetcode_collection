# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        # Time O(nlogn) Space O(N) 
        g = {}
        def f(root: TreeNode, i=0, parents=None):
            if not root:
                return 
            g[root.val] = (i, parents)
            f(root.left, i+1, root.val)
            f(root.right, i+1, root.val)
        f(root)
        return g[x][0] == g[y][0] and g[x][1] != g[y][1] 
        
class Solution:
# Great Solution
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def dfs(node, parent, depth, mod):
            if node:
                if node.val == mod:
                    return depth, parent
                return dfs(node.left, node, depth +1, mod) or dfs(node.right, node, depth+1, mod)
        dx, dy, px, py = dfs(root, None, 0, x) + dfs(root, None, 0, y)
        return dx == px and dy != py

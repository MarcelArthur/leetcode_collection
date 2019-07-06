#!python3
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        # Time O(N) Space O(N)
        if not root:
            return 0
        def dfs(node):
            if not node:
                return (0, 0)
            left = dfs(node.left)
            right = dfs(node.right)
            return (node.val + left[0] + right[0], abs(left[0] - right[0]) + left[1] + right[1])
        res = dfs(root)
        return res[1]
    
class Solution:
    # Space O(N) Time O(N)
    def findTilt(self, root: TreeNode) -> int:
        self.tilt = 0
        self.dfs(root)
        return self.tilt
    def dfs(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.tilt += abs(left - right)
        return left + right + root.val

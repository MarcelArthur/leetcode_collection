class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, float("-inf"))


    def dfs(self, root: TreeNode, max_val: int) -> int:
        if not root:
            return 0
        res = 0
        if max_val <= root.val:
            res += 1
            max_val = root.val

        left_val = self.dfs(root.left, max_val)
        right_val = self.dfs(root.right, max_val)
        return left_val + right_val + res

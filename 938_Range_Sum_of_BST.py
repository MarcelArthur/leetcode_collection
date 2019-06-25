#!python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    """
    第一遍没看懂题意orz
    思路解析: https://www.jianshu.com/p/76e6b9a62688
    """
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        def get_range_sum(root, L, R):
            if not root:
                return 0
            if root.val > R:
                rangesum = get_range_sum(root.left, L, R)
            elif root.val < L:
                rangesum = get_range_sum(root.right, L, R)
            else:
                rangesum = root.val + get_range_sum(root.left, L, R) + get_range_sum(root.right, L, R)
            return rangesum
        return get_range_sum(root, L, R)
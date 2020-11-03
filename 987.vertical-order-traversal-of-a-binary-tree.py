#
# @lc app=leetcode id=987 lang=python3
#
# [987] Vertical Order Traversal of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        res = defaultdict(list)
        queue = [(root, 0)]
        while queue:
            new = []
            curr = defaultdict(list)
            for node, s in queue:
                curr[s].append(node.val)
                if node.left: new.append((node.left, s - 1))
                if node.right: new.append((node.right, s + 1)) 
            for i in curr:
                res[i].extend(sorted(curr[i]))
            queue = new
        return [res[i] for i in sorted(res)]


# @lc code=end


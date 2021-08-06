#
# @lc app=leetcode id=508 lang=python3
#
# [508] Most Frequent Subtree Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        vals = []
        def getSum(root):
            if not root:
                return 0
            
            s = getSum(root.left) + root.val + getSum(root.right)
            vals.append(s)
            return s
        getSum(root)
        res = Counter(vals)
        res_max = max(res.values())
        return [k for k,v in res.items() if v == res_max]


# @lc code=end


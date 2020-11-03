#
# @lc app=leetcode id=590 lang=python3
#
# [590] N-ary Tree Postorder Traversal
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = deque()
        def dfs(root):
            if not root:
                return
            result.appendleft(root.val)
            for i in range(len(root.children)-1, -1, -1):
                dfs(root.children[i])
            return 
        dfs(root)
        return result
                
# @lc code=end


#!python3
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

from typing import List
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        def post_dfs(root, res):
            if root.children:
                for i in root.children:
                    post_dfs(i, res)
            res.append(root.val)

        res = []
        post_dfs(root, res)
        return res

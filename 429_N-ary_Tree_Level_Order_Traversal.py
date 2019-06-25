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
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # 愚蠢的BFS Time O(N) Space O()
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            vaild_res = list()
            one = list()
            for i in stack:
                if i.children:
                    one.extend(i.children)
                vaild_res.append(i.val)
            res.append(vaild_res)
            stack = one
        return res


class Solution:
    # 5-lines Pythoner
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res, q = [], [root]
        while any(q):
            res.append([v.val for v in q])
            q = [child for node in q for child in node.children if node.children]
        return res
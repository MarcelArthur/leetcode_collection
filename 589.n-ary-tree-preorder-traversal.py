#
# @lc app=leetcode id=589 lang=python3
#
# [589] N-ary Tree Preorder Traversal
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
    def preorder(self, root: 'Node') -> List[int]:
        # 1.dfs
        # result = []
        # def dfs(root):
        #     if not root:
        #         return 
        #     result.append(root.val)
        #     if root.children:
        #         for c in root.children:
        #             dfs(c)
        #     return 
        # dfs(root)
        # return result
        # 2. 
        if not root:
            return []
        stack = [root]
        result = list()
        while stack:
            curr = stack.pop()
            result.append(curr.val)
            for i in range(len(curr.children)-1, -1,-1):
                if curr.children[i] != None:
                    stack.append(curr.children[i])
            
        return result
        
        

# @lc code=end


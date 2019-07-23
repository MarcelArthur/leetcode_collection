#!python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution:
    # 普通解法 BFS
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        stack = collections.deque([root])
        result = collections.deque([])
        while stack:
            res = []
            for i in range(len(stack)):
                one = stack.popleft()
                res.append(one.val)
                if one.left:
                    stack.append(one.left)
                if one.right:
                    stack.append(one.right)       
            result.appendleft(res)
        return list(result)
            
class Solution:
    # DFS
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = collections.deque([])
        self.dfs(root, 0, res)
        return list(res)
        
    
    def dfs(self, root: TreeNode, level: int, res: List[int]):
        if not root:
            return 
        if len(res) < level + 1:
            res.appendleft([])
        res[-(level + 1)].append(root.val)
        self.dfs(root.left, level + 1, res)
        self.dfs(root.right, level + 1, res)
        


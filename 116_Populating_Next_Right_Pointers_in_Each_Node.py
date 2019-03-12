"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # if not root:
        #     return root
        # def dfs(left, right):
        if not root:
            return root
        queue = deque([])
        queue.append(root)
        while queue:
            n = len(queue)
            prev = node = None
            for i in range(n):
                prev = node
                node = queue.popleft()
                if i > 0:
                    prev.next = node
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            node.next = None
        return root

# Solution 2
def connect(self, root):
    if not root: return

    currLevel = [root]
    while currLevel:
        nextLevel = []
        for i in range(len(currLevel)-1):
            currNode = currLevel[i]
            currNode.next = currLevel[i+1]
            if currNode.left: nextLevel.append(currNode.left)
            if currNode.right: nextLevel.append(currNode.right)
        
        if currLevel[-1].left: nextLevel.append(currLevel[-1].left)
        if currLevel[-1].right: nextLevel.append(currLevel[-1].right)
        
        currLevel = nextLevel
            

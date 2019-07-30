#!python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Best Solution
class Solution:
    def increasingBST(self, root: TreeNode, tail=None) -> TreeNode:
        if not root:
            return tail
        newRoot = self.increasingBST(root.left, root)
        root.left = None
        root.right = self.increasingBST(root.right, tail)
        return newRoot
        
        
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node: TreeNode) -> TreeNode:
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)
                
        ans = cur = TreeNode(None)
        for v in inorder(root):
            cur.right = TreeNode(v)
            cur = cur.right
        return ans.right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if node:
                inorder(node.left)
                node.left = None
                self.cur.right = node
                self.cur = node
                inorder(node.right)
                
        ans = self.cur = TreeNode(None)
        inorder(root)
        return ans.right
    


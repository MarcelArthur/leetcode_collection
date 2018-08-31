'''
Easy
'''
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
# 递归
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        
        def iter_preorder(node, res):
            res.append(node.val)
            if node.children:
                for n in node.children:
                    iter_preorder(n, res)
        iter_preorder(root, res)
        return res
# 栈
# class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            N = stack.pop()
            result.append(N.val)
            for each in N.children[::-1]:
                if each:
                    stack.append(each)
        return result

            

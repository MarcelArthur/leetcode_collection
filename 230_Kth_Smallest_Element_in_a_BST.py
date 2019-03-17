import bisect
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # My Solution: 不是最优解
        # res = []
        # stack = [root]
        # while stack:
        #     one = stack.pop(0)
        #     bisect.insort(res, one.val)
        #     # res.append(one.val)
        #     if one.left:
        #         stack.append(one.left)
        #     if one.right:
        #         stack.append(one.right)
        # res = sorted(res)
        # return res[k-1]
        
        # Solution 1: DFS实现
        def visit(root: TreeNode) -> None:
            if not root:
                return
            visit(root.left)
            if res:
                return
            count[0] += 1
            if count[0] == k:
                res.append(root.val)
                return
            visit(root.right)
            
        count, res = [0], []
        visit(root)
        return res[0]
    
        # Solution 2:迭代器版本
        def _insorted(root: TreeNode) -> int:
            if root.left is not None:
                for num in _insorted(root.left):
                    yield num
            yield root.val
            if root.right is not None:
                for num in _insorted(root.right):
                    yield num
        count = 0
        for num in _insorted(root):
            count += 1
            if count == k:
                return num
            
        
        

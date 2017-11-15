# !python3
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 寻找二叉搜索树 最初解法: 只考虑到同一层次是否能得到最后的和
# 下面的解法为 通用解法 通过中序遍历得到树的列表 从而可以遍历一整个树的结构


class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        stack = [root]
        while stack:
            for i in range(len(stack) - 1):
                if k == stack[i].val + stack[i + 1].val:
                    return True
            current = stack.pop()
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
        else:
            return False

    def findTarge_Net(self, root, k):
        stack = []
        self.Order_List(root, stack)
        i = 0
        j = len(stack) - 1
        # 通过首尾想加进行夹逼，得到结果是否为Target
        while i < j:
            if stack[i] + stack[j] == k:
                return True
            elif stack[i] + stack[j] < k:
                i += 1
            else:
                j -= 1
        return False

    # 中序遍历得到的是一个中序遍历的结果集
    def Order_List(self, root, rootlist):
        if not root:
            return
        if root.left:
            self.Order_List(root.left, rootlist)
        rootlist.append(root.val)
        if root.right:
            self.Order_List(root.right, rootlist)
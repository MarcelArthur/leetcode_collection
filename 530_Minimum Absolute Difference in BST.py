# !python3
'''
二叉搜索数BST 要么是一个空树，要么是一个具有下列性质的二叉树
1 二叉树的左子树如果非空，那么他所有的左子树的值都小于根节点
2 若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值； 它的左、右子树也分别为二叉排序树
# 定义过多的类方法调用效率不如在类方法中定义一个普通方法

题目:
Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
Note: There are at least two nodes in this BST.

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 我们对于当前结点进行计算：如果当前结点与当前结点的前一个结点的绝对差值小于了当前记录的最小值，那么就更新这个最小值记录（这里要注意 preElement 上一个结点值和 minimum 最小差值的初始值一定要为最大值）
class Solution(object):
    preElement = pow(2, 31) # 定义为最大值
    mininum = pow(2, 31) # 定义为最大值之后使用  有点晕眩X_X

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root.left:
            self.getMinimumDifference(root.left)
        self.mininum = min(self.mininum, abs(root.val - self.preElement))
        self.preElement = root.val
        if root.right:
            self.getMinimumDifference(root.right)
        return self.mininum


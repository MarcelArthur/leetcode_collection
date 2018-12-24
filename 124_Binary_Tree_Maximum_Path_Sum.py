# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Solution 1:思路分析来自https://blog.csdn.net/fly_yr/article/details/50412751
        # 求子树和位最大值的二叉树,最传统的方式是通过递归合并判断处理。这里有两个要点
        # 1 最长子树和位root.left.val + root.right.val + root.val
        # 2 对于每一层递归，只有包含此层树根节点的值才可以返回到上层。否则路径将不连续
        # 3 返回的值最多为根节点加上左右子树中的一个返回值，而不能加上两个返回值。否则路径将分叉。
        # %这里有个很关键的内容是:最大的路径和不一定是直接根节点,可能是子树的某个分支节点累加，但是累加过程不能分叉,只能走左子树和右子树的一支%
        self.maxres = float('-inf')
        def maxSum(root):
            if not root:
                return 0
            curVal = root.val
            lmaxSum = maxSum(root.left)
            rmaxSum = maxSum(root.right)
            if lmaxSum > 0:
                curVal += lmaxSum
            if rmaxSum > 0:
                curVal += rmaxSum
            if curVal > self.maxres:
                self.maxres = curVal
            return max(root.val, max(root.val + lmaxSum, root.val + rmaxSum))
        if not root:
            return 0
        maxSum(root)
        return self.maxres

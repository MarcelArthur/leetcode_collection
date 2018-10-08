# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        '''
        这里其实是根据层次遍历的顺序和前序遍历的顺序列表还原出一个二叉树结构，观察遍历结果可以得出:
        1 层次遍历的首元素是之后元素的根节点
        2 前序遍历的结果值可以根据左子树-根节点-右子树的顺序分离
        3 根据以上顺序可以涉及出深搜形式还原二叉树
        
        解答:
        1 每次从层次遍历列表中弹出首元素,并且查找到根节点所在前序列表中的索引位
        2 构建根节点,左右子树继续向下遍历,通过索引位置左右分离左子树和右子树列表(注意根节点为inx,所有右子树索引位inx + 1)
        
        思路来自LeetCode Discuss中的高票回答
        url: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34579/Python-short-recursive-solution.
        AC 78 % 160ms
        '''
        if inorder:
            inx = inorder.index(preorder.pop(0))
            new_tree = TreeNode(inorder[inx])
            new_tree.left = self.buildTree(preorder, inorder[:inx])
            new_tree.right = self.buildTree(preorder, inorder[inx+1:])
            return new_tree

        
    

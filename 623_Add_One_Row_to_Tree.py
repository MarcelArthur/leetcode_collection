class Solution:
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        '''
        1. 计算超时= =, 不过求解思路没问题, 需要注意的是在d即树深更新的时候当d=1时意味着最后一层二叉树之前要进行添加节点的操作，所以这里的树深是倒数一层的二叉树之前进行添加节点的工作，另外需要注意的是树神只有1是需要在原节点上构建一个新的根节点，这点尤为需要注意
        '''
        # if not root:
        #     return
        # if d == 1:
        #     tree = TreeNode(v)
        #     tree.left = root
        #     return tree
        # q = [root]
        # while q:
        #     d -= 1
        #     if d == 0:
        #         return 
        #     n = len(q)
        #     for i in range(n):
        #         pop_one = q.pop(0)
        #         if d == 1:
        #             left = root.left
        #             right = root.right
        #             pop_one.left = TreeNode(v)
        #             pop_one.right = TreeNode(v)
        #             pop_one.left.left = left
        #             pop_one.right.right = right
        #         else:
        #             if pop_one.left:
        #                 q.append(pop_one.left)
        #             else:
        #                 q.append(pop_one.right)
        # return root
        
        '''
        2 递归求解
        大神操作-这里的解释引用自博客Grandyang, 虽然在Python3中递归性能不好，但是作为一种解题思路可以记一下
        url:https://www.cnblogs.com/grandyang/p/7070182.html
        "
        这里d的0和1，其实相当于一种flag，如果d为1的话，那么将root连到新建的结点的左子结点上；反之如果d为0，那么将root连到新建的结点的右子结点上，然后返回新建的结点。如果root存在且d大于1的话，那么对root的左子结点调用递归函数，注意此时若d的值正好为2，那么我们就不能直接减1，而是根据左右子结点的情况分别赋值1和0。
        "
        '''
        if (d == 0) or (d == 1):
            newRoot = TreeNode(v)
            if d:
                newRoot.left = root
            else:
                newRoot.right = root
            return newRoot
        if root and d > 1:
            root.left = self.addOneRow(root.left, v, (d - 1) if d > 2 else 1)
            root.right = self.addOneRow(root.right, v, (d - 1) if d > 2 else 0)
        return root
    
        
        
    
    

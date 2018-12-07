class Solution:
    # def isSubtree(self, s, t):
    #     """
    #     :type s: TreeNode
    #     :type t: TreeNode
    #     :rtype: bool
    #     """
    #     # Solution 1:
    #     # dfs 二叉树子树匹配问题（转化为Same Tree更好理解）
    #     # 这里实际上使用两个递归函数进行判断首先是通过isSubtree逐层向下进行递归，同时通过issanme判断两个子树是否同时满足所有条件，
    #     if not s:
    #         return False
    #     if self.isSame(s, t):
    #         return True
    #     return self.isSubtree(s.left, t) | self.isSubtree(s.right, t)
    # def isSame(self, s, t):
    #     if not s and not t:
    #         return True
    #     if not s or not t:
    #         return False
    #     if s.val != t.val:
    #         return False
    #     return self.isSame(s.left, t.left) & self.isSame(s.right, t.right)
    
        # Solution 2:
        # 将二叉树s和二叉树t序列化为字符串，如果二叉树在二叉树s中存在且为子树关系则返回Ture，否则为False(由于python中的字符串为不可变量，所以遍历累加的过程改为列表实现，最后转化为序列化字符串进行比较) Runtime 132ms AC85% 
        # Tips：关于特例[12], [2]实际上[2]并不是[12]的子树，所以在每个结点前用“,”分割，',12#'和’，2#‘则为不同子树，结果为False
    def isSubtree(self, s, t):
        sc, tc = [], []
        self.serialize(s, sc)
        self.serialize(t, tc)
        sc = ''.join(sc)
        tc = ''.join(tc)
        return sc.find(tc) != -1
    def serialize(self, node, c):
        if not node:
            c.append(',#')
        else:
            c.append(',' + str(node.val))
            self.serialize(node.left, c)
            self.serialize(node.right, c)
        
        
        

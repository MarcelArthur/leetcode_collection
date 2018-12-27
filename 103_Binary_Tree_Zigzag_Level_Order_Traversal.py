# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # Solution 1:
        # 深度遍历(前序遍历)存储到对应到层级字典当中，之后对于字典key重新排序,再次遍历所有层级进行判断处理:
        # 奇数层级: 逆序输出
        # 偶数层级: 正常输出
        # 时间复杂度O(N) AC 40% 
        cnt = 0
        self.cntOrder = dict()
        def LevelOrder(root, cnt):
            if not root:
                return 
            self.cntOrder[cnt] = self.cntOrder.get(cnt, [])
            self.cntOrder[cnt].append(root.val)
            LevelOrder(root.left, cnt + 1)
            LevelOrder(root.right, cnt + 1)
        LevelOrder(root, cnt)
        Levelkey = [x for x in self.cntOrder.keys()]
        Levelkey.sort()
        cntResult = []
        for x in Levelkey:
            if x % 2 == 1:
                cntResult.append(self.cntOrder[x][::-1])
            else:
                cntResult.append(self.cntOrder[x])
        
        return cntResult
    
        # Solution 2:
        # 线性时间复杂度实现
        # 时间复杂度O(N),空间复杂度O(N)
        
    def zigzagLevelOrder(self, root):
        ZIG,ZAG = 0,1 # zig from left-to-right, zag from right-to-left
        cur_dir = ZIG
        coll = [] if root is None else [root]
        result = []
        
        while coll:
            elems = coll if cur_dir == ZIG else coll[::-1]
            result += [[elem.val for elem in elems]]
            coll = [child for node in coll for child in [node.left, node.right] if child is not None]
            cur_dir = (cur_dir + 1) % 2 
        
        return result
        
    
                
            

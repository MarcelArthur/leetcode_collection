class TreeNode:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val
        self.count = 1
        
class Solution:
    def insertTree(self, root, val):
        if not root:
            return 0
        tempCount = 0 
        while True:
            if val <= root.val:
                root.count += 1
                if root.left is None:
                    root.left = TreeNode(val)
                    break
                else:
                    root = root.left
            else:
                tempCount += root.count
                if root.right is None:
                    root.right = TreeNode(val)
                    break
                else:
                    root = root.right
        return tempCount
                
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Solution 1: 时间复杂度O(N!),每pop出左侧的一个数字必须遍历剩余的数字获取小于该数字的数字个数, TLE预定。
        # Solution 2: BST
        # Solution 3: 线段树求解
        
        n = len(nums)
        if n == 0:
            return []
        if n == 1:
            return [0]
        
        ans = []
        root = TreeNode(nums[-1])
        ans.append(0)
        
        for i in range(n-2, -1, -1):
            count = self.insertTree(root, nums[i])
            ans.append(count)
        return ans[::-1]

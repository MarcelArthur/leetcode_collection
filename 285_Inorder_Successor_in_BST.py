class Solution:
    node = None
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root or not p:
            return None
        
        self.dfs(root, p)
        return self.node
    
    def dfs(self, root, p):
        if not root:
            return 
        if p.val < root.val:
            if self.node is None or self.node.val > root.val:
                self.node = root
            self.dfs(root.left, p)
        else:
            self.dfs(root.right, p)
            

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Codec:
    #  Solution 1:深度遍历(前序遍历)序列化和反序列化的方式
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ser = []
        def preOrder(root):
            if not root:
                ser.append('#')
            else:
                ser.append(str(root.val))
                preOrder(root.left)
                preOrder(root.right)
        preOrder(root)
        return ' '.join(ser)
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = collections.deque([x for x in data.split()])
        def build():
            if vals:
                val = vals.popleft()
                if val == '#':
                    return None
                else:
                    root = TreeNode(int(val))
                    root.left = build()
                    root.right = build()
                return root
        return build()
    # Solution 2: 层次遍历序列化和反序列化的方式
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        ser = []
        serroot = [root]
        while serroot:
            rootone = serroot.pop(0)
            if rootone:
                ser.append(str(rootone.val))
                serroot.append(rootone.left)
                serroot.append(rootone.right)
            else:
                ser.append('#')
        return ' '.join(ser)
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        curdata = collections.deque()
        cur = None
        vals = collections.deque([x for x in data.split()])
        if vals:
            val = vals.popleft()
            if val != '#':
                cur = TreeNode(val)
                curdata.append(cur)
        while vals and curdata:
            val = vals.popleft()
            curone = curdata.popleft()
            if not val:
                break
            if val != '#':
                curleft = TreeNode(val)
                curone.left = curleft
                curdata.append(curleft)
            val = vals.popleft()
            if not val:
                break
            if val != '#':
                curright = TreeNode(val)
                curone.right = curright
                curdata.append(curright)
        return cur
            
                
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

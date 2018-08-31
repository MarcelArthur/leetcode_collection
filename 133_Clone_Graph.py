# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
# BFS遍历
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self.dict = {None: None}
    def cloneGraph(self, node):
        if node == None:
            return None
        head = UndirectedGraphNode(node.label)
        self.dict[node] = head
        for n in node.neighbors:
            if n in self.dict:
                head.neighbors.append(self.dict[n])
            else:
                neigh = self.cloneGraph(n)
                head.neighbors.append(neigh)
        return head
        
        

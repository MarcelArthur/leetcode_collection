class Solution:
    def allPathsSourceTarget(self, graph: 'List[List[int]]') -> 'List[List[int]]':
        # https://leetcode.com/problems/all-paths-from-source-to-target/discuss/225236/Easy-BFS-and-DFS-Solutions-Python
        # bfs
        q = []
        result = []
        q.append((0, [0]))
        
        while q:
            index, path = q.pop()
            if index == len(graph) - 1:
                result.append(path)
            for neighbor in graph[index]:
                q.insert(0, (neighbor, path + [neighbor]))
            
        return result
    
        # dfs
#         def dfs(index: 'int', q: 'List[int]') -> 'None':
#             if index == len(graph) - 1:
#                 result.append(q)
#             for val in graph[index]:
#                 dfs(val, q + [val])
            
#         result = []
#         dfs(0, [0])
#         return result
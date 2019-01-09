import collections
class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        # 与Course Schedule题目类型相似，只不过在这里是判断DAG(有向无环图)，如果存在这里只能返回空列表，否则可以返回修完所有课程的顺序。
        # Solution 1:DFS
        # 参考资料: https://blog.csdn.net/fuxuemingzhu/article/details/83302328#_139
        graph = collections.defaultdict(list)
        
        for u, v in prerequisites:
            graph[u].append(v)
        path = []
        visited = [0] * numCourses
        
        for i in range(numCourses):
            if not self.dfs(graph, path, i, visited):
                return []
        return path
    
    def dfs(self, graph, path, i, visited):
        if visited[i] == 1:
            return False
        if visited[i] == 2:
            return True
        
        visited[i] = 1
        for j in graph[i]:
            if not self.dfs(graph, path, j, visited):
                return False
        visited[i] = 2
        path.append(i)
        return True

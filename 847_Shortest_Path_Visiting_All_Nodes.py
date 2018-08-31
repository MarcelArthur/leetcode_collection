class Solution:
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        # 了解无向图的遍历方式, 以及最短路径的解法, 问题以邻接表的方式展现无向图的类型
        # 目前看到的解法是1. Floyd + 动态规划
        # 2.BFS可以AC, 位运算判断是否是重复路径
        # 3.告诉实现
        # 2 BFS, 遍历的同事进行剪枝
        if len(graph) == 1:
            return 0
        step = 1
        q, qq = [(i, 1<<i) for i in range(len(graph))], []
        vis = set(q)
        while q:
            while q:
                i, s = q.pop()
                if s == ((1 << len(graph)) - 1):
                    return step - 1
                for t in graph[i]:
                    if (t, s|(1<<t)) not in vis:
                        qq.append((t, s|1<<t))
                        vis.add((t, s|1<<t))
            q,qq = qq,q
            step += 1

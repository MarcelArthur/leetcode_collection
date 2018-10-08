from collections import defaultdict
'''
Solution 1:
搜索边列表
实际上这个是一个实时搜索的判定问题，如果搜索结果是一个环，则认为搜索返回为False,实际上是在标记的同时进行深搜，确认连接的列表中没有任何一个图/子图是环形图。
实质是将边列表转化成邻接矩阵的形式。
同理这种标记方式可以替换为集合的方式进行处理,思路类似。代码如下,以下通过邻接矩阵标记访问节点查看是否为环形。
'''
class Solution:
    def canFinish(self, N, edges):
        pre = defaultdict(list)
        for x, y in edges: pre[x].append(y)

        status = [0] * N
        def canTake(i):
            if status[i] in {1, -1}: 
                return status[i] == 1
            status[i] = -1
            if any(not canTake(j) for j in pre[i]): 
                return False
            status[i] = 1
            return True

        return all(canTake(i) for i in range(N))

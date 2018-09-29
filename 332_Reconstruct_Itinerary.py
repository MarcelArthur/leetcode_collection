import collections
class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        """
        1 图遍历的逻辑 标记使用过的节点 时间复杂度最大为O((n^2 + n)/2), 最小时间复杂度为O(n) 不推荐
        2 欧拉图和欧拉通路，半欧拉图 (通过有向图和无向图中所有的边，且每条边只走一次的通路称为欧拉通路； 可以相应的回路称为欧拉回路，具有欧拉回路的图称为欧拉图；具有欧拉通路没有欧拉回路的称为半欧拉图)
        
        
        solution1: 通过collection构建欧拉图，进行回溯边路结果 
        solution2: DFS遍历所有路径，标记内容移除遍历过得路径，递归进行归并得出最后的结果
        
        """
        # abc = list(map(judege_arrival, tickets)) 
        # Python3中的map实现 使用懒加载 (节省性能) 如果不对map对象执行list()方法转化是不会执行得到map函数的结果的(坑爹)
        # Solution1
        routeresult = []
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a] += [b]
        
        def visit(node):
            while targets[node]:
                visit(targets[node].pop())
            routeresult.append(node)
        visit("JFK")
        return routeresult[::-1]
        # Solution2
#         route_target = collections.defaultdict(list)
#         for s, d in tickets:
#             route_target[s].append(d)
        
#         def solve(start):
#             left, right = [], []
#             for end in sorted(route_target[start]):
#                 if end not in route_target[start]:
#                     continue
#                 route_target[start].remove(end)
#                 subresult = solve(end)
#                 if start in subresult:
#                     left += subresult
#                 else:
#                     right += subresult
#             return [start] + left +right
#         return solve("JFK")
        
        
        
        

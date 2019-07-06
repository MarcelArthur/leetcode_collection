#!python3
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        Space O(1) Time O(nlgn)
        """
        if not stones:
            return 0
        while len(stones) > 1:
            stones.sort()
            a, b = stones.pop(), stones.pop()
            if a != b:
                v = abs(a-b)
                stones.append(v)
        return stones[0] if stones else 0
class Solution:
    # 推排序，heap库
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = [-x for x in stones]
        heapq.heapify(pq)
        for i in range(len(stones) - 1):
            x, y = -heapq.heappop(pq), -heapq.heappop(pq)
            heapq.heappush(pq, -abs(x - y))
        return -pq[0]

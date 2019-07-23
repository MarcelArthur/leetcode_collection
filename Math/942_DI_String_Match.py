#!python3
class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        if not S:
            return []
        r = collections.deque([x for x in range(len(S) + 1)])
        res = []
        for i, v in enumerate(S):
            if v == "I":
                res.append(r.popleft())
            else:
                res.append(r.pop())
        return res + list(r)

class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        if not S:
            return []
        res = []
        left = 0
        right = len(S) 
        for i, v in enumerate(S):
            if v == "I":
                res.append(left)
                left += 1
            else:
                res.append(right)
                right -= 1
        res.append(left)
        return res

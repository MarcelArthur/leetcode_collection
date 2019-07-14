#!python3
class Solution:
    # 996 ICU 
    # https://leetcode.com/problems/longest-well-performing-interval/discuss/334565/JavaC%2B%2BPython-O(N)-Solution-Life-needs-996-and-669
    def longestWPI(self, hours: List[int]) -> int:
        res = score = 0
        seen = {0: -1}
        for i, v in enumerate(hours):
            score = score + 1 if v > 8 else score - 1
            if score > 0:
                res = i + 1
            if score not in seen:
                seen[score] = i
            if score - 1 in seen:
                res = max(res, i - seen[score -1])
        return res

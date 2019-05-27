#!python3
from typing import List
"""
691. Stickers to Spell Word

address: https://leetcode.com/problems/stickers-to-spell-word/

We are given N different types of stickers. Each sticker has a lowercase English word on it.

You would like to spell out the given target string by cutting individual letters from your collection of stickers and rearranging them.

You can use each sticker more than once if you want, and you have infinite quantities of each sticker.

What is the minimum number of stickers that you need to spell out the target? If the task is impossible, return -1.

Example 1:

Input:

["with", "example", "science"], "thehat"
Output:

output:
3
"""
import collections


class Solution:
    def __init__(self):
        self.ana = None

    # Solution 1: DFS
    def minStickers(self, stickers: List[str], target: str) -> int:
        stickers, self.map = [collections.Counter(s) for s in stickers if set(s) & set(target)], {}

        def dfs(target):
            if not target:
                return 0
            if target in self.map:
                return self.map[target]
            cnt, res = collections.Counter(target), float('inf')
            for c in stickers:  # traverse the stickers to get new target
                if c[target[0]] == 0:
                    continue  # we can make sure the 1st letter will be removed to reduce the time complexity
                nxt = dfs(''.join([s * t for (s, t) in (cnt - c).items()]))
                if nxt != -1:
                    res = min(res, 1 + nxt)
            self.map[target] = -1 if res == float('inf') else res
            return self.map[target]
        return dfs(target)

    # Solution 2: DP 动态规划 TLE 时间复杂度太高
    # to change minSticker
    def minStickers_solution(self, stickers: List[str], target: str) -> int:
        n = len(target)
        m = 1 << n
        dp = [float('inf')] * m
        dp[0] = 0
        for i in range(m):
            if dp[i] == float('inf'):
                continue
            for sticker in stickers:
                cur = i
                for c in sticker:
                    for k in range(n):
                        if target[k] == c and ((cur >> k) & 1) == 0:
                            cur |= 1 << k
                            break
                dp[cur] = min(dp[cur], dp[i] + 1)
        return -1 if dp[m - 1] == float('inf') else dp[m-1]







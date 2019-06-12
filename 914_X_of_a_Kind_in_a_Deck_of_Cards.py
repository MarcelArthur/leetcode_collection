#!python3
from typing import List
import collections


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        col = collections.Counter(deck)
        min_size = len(col.values())

        for i in range(min_size + 1, 1, -1):
            res = all(value % i == 0 for value in col.values())
            if res:
                return True
        return False

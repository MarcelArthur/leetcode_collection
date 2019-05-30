#!python3
from typing import List


class Solution:
    """
    https://leetcode.com/problems/find-smallest-letter-greater-than-target/discuss/287287/python-BST-2-solutions-non-recursive-recursive-92-99-faster
    """

    # Solution 1: Using BST while loop
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1] or target < letters[0]:
            return letters[0]
        s, e = 0, len(letters) - 1
        while s <= e:
            mid = (s + e) // 2

            if letters[mid - 1] <= target < letters[mid]:
                return letters[mid]
            if target >= letters[mid]:
                s = mid + 1
            else:
                e = mid

    # Solution 2: Using BST, Above code coverted into recursion
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1] or target < letters[0]:
            return letters[0]
        return self.helpfunc(letters, 0, len(letters) - 1, target)

    def helpfunc(self, letters: List[str], start: int, end: int, target: str) -> str:
        mid = (start + end) // 2
        if letters[mid - 1] <= target < letters[mid]:
            return letters[mid]

        if target >= letters[mid]:
            return self.helpfunc(letters, mid + 1, end, target)
        else:
            return self.helpfunc(letters, start, mid, target)
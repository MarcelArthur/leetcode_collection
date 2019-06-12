#!python3
from typing import List
"""
We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words. 

You may return the list in any order.

 

Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: A = "apple apple", B = "banana"
Output: ["banana"]
 

Note:

0 <= A.length <= 200
0 <= B.length <= 200
A and B both contain only spaces and lowercase letters.


# Simple Solution Time O(N) Space O(N)
class Solution:
    def uncommonFromSentences_second(self, A: str, B: str) -> List[str]:
        both = A.split(" ") + B.split(" ")
        return [x for x in both if both.count(x) == 1]
"""


class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        if not A and not B:
            return []
        uncommon = dict()
        result = list()
        Z = A.split(" ") + B.split(" ")
        for v in Z:
            uncommon[v] = uncommon.get(v, 0) + 1
            if uncommon.get(v) == 1:
                result.append(v)
            elif uncommon.get(v) == 2:
                result.remove(v)
        return result





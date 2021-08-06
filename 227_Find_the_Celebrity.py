# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        # https://leetcode.com/problems/find-the-celebrity/discuss/71228/JavaPython-O(n)-calls-O(1)-space-easy-to-understand-solution
        # The first of Understand the meaning of the question
        if not n:
            return -1
        x = 0 
        for i in range(n):
            if knows(x, i):
                x = i
        if any(knows(x, i) for i in range(x)):
            return -1
        if any(not knows(i, x) for i in range(n)):
            return -1
        return x
